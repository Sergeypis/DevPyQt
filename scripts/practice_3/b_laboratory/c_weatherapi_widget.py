"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""
import time

from PySide6 import QtWidgets, QtCore, QtGui
from scripts.practice_3.b_laboratory.a_threads import WeatherHandler
from scripts.practice_3.b_laboratory.ui.weather_widget import Ui_weather_form


class WeatherWindow(QtWidgets.QWidget):
    # status_bar_signal = QtCore.Signal(str)
    # exit_syswindow_signal = QtCore.Signal(bool)
    # settings = QtCore.QSettings('d_eventfilter_settings.ini', QtCore.QSettings.IniFormat)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.thread_weather = None

        self.initThreads()
        self.ui_weather = Ui_weather_form()
        self.ui_weather.setupUi(self)
        self.add_setupUi()

        self.initSignals()
        self.load_settings()
        # self.start_weather_thread()

    def add_setupUi(self):
        """
        Доинициализация Ui

        :return: None
        """

        self.move(self.screen().geometry().center().x() + 220, \
                  self.screen().availableGeometry().center().y() - self.frameSize().height()//2)

    def load_settings(self) -> None:
        """
        Загрузка настроек в Ui

        :return: None
        """
        pass

    def initThreads(self):
        """
        Инициализация потоков

        :return: None
        """

        # self.thread_sys = SystemInfo()
        # self.thread_sys.start()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Событие закрытия окна

        :param event: QtGui.QCloseEvent
        :return: None
        """

        answer = QtWidgets.QMessageBox.question(
            self, "Закрыть окно?", "Вы действительно хотите закрыть окно?"
        )

        if answer == QtWidgets.QMessageBox.StandardButton.Yes:
            # self.thread_sys.stop_sys_thread()
            # self.thread_sys.quit()
            time.sleep(1)
            event.accept()
            # self.exit_syswindow_signal.emit(None)
        else:
            event.ignore()

    # settings -----------------------------------------------------------

    # events -----------------------------------------------------------

    # signals ----------------------------------------------------------
    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        pass
        # self.thread_sys.started.connect(self.set_start_signal)
        # self.thread_sys.finished.connect(self.thread_sys.deleteLater)
        # self.thread_sys.finished.connect(self.set_finish_signal)

    # slots --------------------------------------------------------------

    # def start_weather_thread(self) -> None:
    #     self.thread_weather.start()

