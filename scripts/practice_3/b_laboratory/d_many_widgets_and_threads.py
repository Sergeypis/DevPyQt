"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
import os
import sys
import time
import platform
import subprocess

from PySide6 import QtWidgets, QtCore

from b_systeminfo_widget import SysWindow
from c_weatherapi_widget import WeatherWindow
from ui.main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    main_window_created = False

    def __init__(self, parent=None):
        super().__init__(parent)
        self.check_double_window()

        # self.sys_window = None
        # self.wether_window = None

        self.ui_main = Ui_MainWindow()

        self.ui_main.setupUi(self)
        # self.add_setupUi()

        # self.load_settings()
        self.initSignals()

    # @classmethod
    # def information_message(cls):
    #         msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, f"Ошибка",
    #                     f"Произведена попытка запустить вторую копию приложения ",
    #                     QtWidgets.QMessageBox.StandardButton.Ok, None)
    #         msg_box.setInformativeText("Одновременно два окна приложения не могут быть запущены!")
    #         reply = msg_box.exec()
    #         if reply == QtWidgets.QMessageBox.StandardButton.Ok:
    #             return None
    #
    # @classmethod
    # def check_double_window(cls):
    #     if cls.main_window_created:
    #         cls.information_message()
    #         sys.exit()
    #     else:
    #         cls.main_window_created = True

    def check_double_window(self):
        p = subprocess.Popen(f'tasklist /FI "IMAGENAME eq {os.path.basename(sys.argv[0])}" /FO "LIST"', stdout=subprocess.PIPE, text=True)
        out, _ = p.communicate()
        if out.count((sys.argv[0].rsplit('\\', 1)[1])) >= 2:
            # sys.stderr.write('program is already running')
            sys.exit()

    # settings -----------------------------------------------------------

    # events -----------------------------------------------------------

    # signals ---------------------------------------------------------
    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.ui_main.pb_open_sys_widget.clicked.connect(self.on_start_sys_widget)
        self.ui_main.pb_open_weath_widget.clicked.connect(self.on_start_weather_widget)
        self.ui_main.exit_app_menu.triggered.connect(QtCore.QCoreApplication.instance().exit)

    # slots --------------------------------------------------------------
    def on_start_sys_widget(self):
        """
        Запускает окно информации о загрузке системы
        :return: None
        """
        self.sys_window = SysWindow()
        self.sys_window.show()
        self.sys_window.status_bar_signal.connect(self.ui_main.statusbar.showMessage)

    def on_start_weather_widget(self):
        """
        Запускает окно запроса прогноза погоды
        :return: None
        """
        self.weather_window = WeatherWindow()
        self.weather_window.show()
        self.weather_window.status_bar_signal.connect(self.ui_main.statusbar.showMessage)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    # if MainWindow.main_window_created:
    #     sys.exit()

    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
