"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
import os
import sys
import time
import platform
import subprocess

from PySide6 import QtWidgets, QtCore
from shiboken6 import delete

from b_systeminfo_widget import SysWindow
from c_weatherapi_widget import WeatherWindow
from ui.main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.check_double_window()

        self.sys_window = None
        self.weather_window = None

        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)

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

    @staticmethod
    def check_double_window():
        p = subprocess.Popen(f'tasklist /FI "IMAGENAME eq {os.path.basename(sys.argv[0])}" /FO "LIST"', stdout=subprocess.PIPE, text=True)
        out, _ = p.communicate()
        if out.count((sys.argv[0].rsplit('\\', 1)[1])) >= 2:
            # sys.stderr.write('program is already running')
            sys.exit()

    @staticmethod
    def on_close():
        QtCore.QCoreApplication.instance().exit()
        # sys.exit()

    # settings -----------------------------------------------------------

    # events -----------------------------------------------------------
    def closeEvent(self, event):
        self.on_close()

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
        if self.sys_window is None:
            self.sys_window = SysWindow()
            self.sys_window.show()

            self.sys_window.status_bar_signal.connect(self.ui_main.statusbar.showMessage)
            self.sys_window.on_close_signal.connect(self.sys_window_closed)

    def sys_window_closed(self):
        self.ui_main.statusbar.clearMessage()
        self.sys_window = None

    def on_start_weather_widget(self):
        """
        Запускает окно запроса прогноза погоды
        :return: None
        """
        # print(self.weather_window)
        if self.weather_window is None:
            self.weather_window = WeatherWindow()
            self.weather_window.show()

            self.weather_window.status_bar_signal.connect(self.ui_main.statusbar.showMessage)
            self.weather_window.on_close_signal.connect(self.weather_window_closed)

    def weather_window_closed(self):
        self.ui_main.statusbar.clearMessage()
        self.weather_window = None


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
