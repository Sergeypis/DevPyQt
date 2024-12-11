"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""
import datetime
import sys
import time, re

from PySide6 import QtWidgets, QtCore, QtGui
from a_threads import WeatherHandler
from ui.weather_widget import Ui_weather_form


class WeatherWindow(QtWidgets.QWidget):
    # weather_window_created = False
    status_bar_signal = QtCore.Signal(str)
    on_close_signal = QtCore.Signal()

    # def __new__(cls):
    #     if cls.check_double_window():
    #         return None
    #     else:
    #         return super().__new__(cls)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.thread_weather = None
        self.__lat = None
        self.__lon = None

        self.initThreads()
        self.ui_weather = Ui_weather_form()
        self.ui_weather.setupUi(self)
        self.add_setupUi()

        self.initSignals()
        self.load_settings()

    # @classmethod
    # def information_message(cls):
    #         msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, f"Ошибка",
    #                     f"Произведена попытка запустить вторую копию окна ",
    #                     QtWidgets.QMessageBox.StandardButton.Ok, None)
    #         msg_box.setInformativeText("Одновременно два окна приложения не могут быть запущены!")
    #         reply = msg_box.exec()
    #         if reply == QtWidgets.QMessageBox.StandardButton.Ok:
    #             return None
    #
    # @classmethod
    # def check_double_window(cls):
    #     if cls.weather_window_created:
    #         cls.information_message()
    #         return True
    #     else:
    #         cls.weather_window_created = True
    #         return False

    @staticmethod
    def is_valid_coord(coord: str) -> bool:
        pattern = re.compile('^(?:-?\d{,3}.\d{,6})$')
        return bool(pattern.match(coord))

    def add_setupUi(self):
        """
        Доинициализация Ui

        :return: None
        """

        self.move(self.screen().geometry().center().x() + 222, \
                  self.screen().availableGeometry().center().y() - self.frameSize().height()//2)

    def load_settings(self) -> None:
        """
        Загрузка настроек в Ui

        :return: None
        """
        self.get_latitude()
        self.get_longitude()

    def initThreads(self):
        """
        Инициализация потоков

        :return: None
        """
        self.thread_weather = WeatherHandler('','')
        # self.thread_weather = WeatherHandler()

    def get_delay(self) -> int:
        """
        Получает данные из полей ввода задержки и преобразовывает к секундам

        :return: Задержку в секундах типа int
        """
        delay = self.ui_weather.input_delay.text()
        units = self.ui_weather.cb_units_duration.currentText()
        mul = {'сек': 1, 'мин': 60, 'час': 3600}
        return int(delay) * mul[units]

    def on_close(self):
        """
        Действия при закрытии окна WeatherWindow
        """
        if self.thread_weather.isRunning():
            self.start_and_stop_thread()
            while self.thread_weather.isRunning():
                time.sleep(0.1)
        # time.sleep(0.5)

    # settings -----------------------------------------------------------

    # events -----------------------------------------------------------
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Событие закрытия окна

        :param event: QtGui.QCloseEvent
        :return: None
        """
        answer = QtWidgets.QMessageBox.question(self, "Закрыть окно?", "Вы действительно хотите закрыть окно?")

        if answer == QtWidgets.QMessageBox.StandardButton.Yes:
            self.on_close()
            event.accept()
            self.on_close_signal.emit()
        else:
            event.ignore()

    # signals ----------------------------------------------------------
    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.ui_weather.pb_get_data.clicked.connect(self.start_and_stop_thread)
        self.ui_weather.input_lat.textChanged.connect(self.get_latitude)
        self.ui_weather.input_lon.textChanged.connect(self.get_longitude)

    # slots --------------------------------------------------------------
    def get_latitude(self) -> None:
        """
        Забирает координаты из поля ввода широты.
        Проводит валидацию введенных координат.

        :return: None
        """
        coord = self.ui_weather.input_lat.text()
        if self.is_valid_coord(coord):
            self.__lat = coord
            self.ui_weather.output_field.clear()
            self.ui_weather.pb_get_data.setEnabled(True)
        else:
            self.ui_weather.output_field.setPlainText("Координата широты введена неверно, повторите ввод!")
            self.ui_weather.pb_get_data.setEnabled(False)

    def get_longitude(self) -> None:
        """
        Забирает координаты из поля ввода долготы.
        Проводит валидацию введенных координат.

        :return: None
        """
        coord = self.ui_weather.input_lon.text()
        if self.is_valid_coord(coord):
            self.__lon = coord
            self.ui_weather.output_field.clear()
            self.ui_weather.output_field.clear()
            self.ui_weather.pb_get_data.setEnabled(True)
        else:
            self.ui_weather.output_field.setPlainText("Координата долготы введена неверно, повторите ввод!")
            self.ui_weather.pb_get_data.setEnabled(False)

    def block_fields_on_start(self):
        self.ui_weather.input_lon.setEnabled(False)
        self.ui_weather.input_lat.setEnabled(False)
        self.ui_weather.input_delay.setEnabled(False)
        self.ui_weather.cb_units_duration.setEnabled(False)
        self.ui_weather.pb_get_data.setText("Остановить опрос")

    def unblock_fields_on_stop(self):
        self.ui_weather.input_lon.setEnabled(True)
        self.ui_weather.input_lat.setEnabled(True)
        self.ui_weather.input_delay.setEnabled(True)
        self.ui_weather.cb_units_duration.setEnabled(True)
        self.ui_weather.pb_get_data.setText("Получить данные")

    def create_signal_for_statusbar(self):
        self.status_bar_signal.emit(f'Запущен поток {self.__class__.__name__}')

    def create_finish_signal(self):
        self.status_bar_signal.emit(f'Поток {self.__class__.__name__} остановлен')
        self.ui_weather.output_field.appendPlainText(f"Работа API Weather Thread завершена")

    def weather_data_handler(self, data: dict):
        if data.get('error'):
            self.ui_weather.output_field.insertPlainText(f"Ошибка запроса: {data.get('reason')}")
            self.start_and_stop_thread()
        else:
            parse_data = [
                f"Дата и время: {datetime.datetime.now()}",
                f"Широта: {data.get('latitude', '---')}",
                f"Долгота: {data.get('longitude', '---')}",
                f"Температура: {data.get('current_weather').get('temperature', '---')}\
{data.get('current_weather_units').get('temperature', '---')}",
                f"Скорость ветра: {data.get('current_weather').get('windspeed', '---')}\
{data.get('current_weather_units').get('windspeed', '---')}",
                f"Направление ветра: {data.get('current_weather').get('winddirection', '---')}\
{data.get('current_weather_units').get('winddirection', '---')}",
            ]
            self.ui_weather.output_field.setPlainText('\n'.join(parse_data))

    def start_and_stop_thread(self) -> None:
        """
        Запускает и останавливает поток (цикл while в thread_weather.run())

        :return: None
        """

        if not self.thread_weather.status:
            self.ui_weather.output_field.clear()
            self.thread_weather = WeatherHandler(self.__lat, self.__lon)
            self.thread_weather.setDelay(self.get_delay())
            self.thread_weather.status = True
            self.thread_weather.start()
            self.thread_weather.started.connect(self.block_fields_on_start)
            self.thread_weather.started.connect(self.create_signal_for_statusbar)
            self.thread_weather.weatherdataSignal.connect(self.weather_data_handler)
        else:
            self.thread_weather.status = False
            self.thread_weather.finished.connect(self.unblock_fields_on_stop)
            self.thread_weather.finished.connect(self.create_finish_signal)

