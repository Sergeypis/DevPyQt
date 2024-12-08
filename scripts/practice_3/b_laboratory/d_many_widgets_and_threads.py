"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
import sys
import time

from PySide6 import QtWidgets, QtCore

from scripts.practice_3.b_laboratory.b_systeminfo_widget import SysWindow
from scripts.practice_3.b_laboratory.c_weatherapi_widget import WeatherWindow
from scripts.practice_3.b_laboratory.ui.main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    window_create = False

    def __init__(self, parent=None):
        super().__init__(parent)
        # self.sys_window = None

        # self.wether_window = None

        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)
        # self.add_setupUi()

        # self.load_settings()
        self.initSignals()

        MainWindow.window_create = True

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

    if MainWindow.window_create:
        sys.exit()

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
