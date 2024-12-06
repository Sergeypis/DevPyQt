"""
Модуль в котором содержаться потоки Qt
"""

import time

import psutil
import requests
from PySide6 import QtCore
# from scripts.practice_3.b_laboratory.d_many_widgets_and_threads import MainWindow


class SystemInfo(QtCore.QThread):
    systemInfo_signal = QtCore.Signal(list)  # Создайте экземпляр класса Signal и передайте ему в конструктор тип данных передаваемого значения (в текущем случае list)
    thread_delay_signal = QtCore.Signal(float)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None  # создайте атрибут класса self.delay = None, для управлением задержкой получения данных

    def set_delay(self, delay: float) -> None:
        self.delay = delay

    def run(self) -> None:  # переопределить метод run
        if self.delay is None:  # Если задержка не передана в поток перед его запуском
            self.delay = 1  # то устанавливайте значение 1

        while True:  # Запустите бесконечный цикл получения информации о системе
            self.thread_delay_signal.connect(self.set_delay)
            cpu_value = psutil.cpu_percent(0.2)  # с помощью вызова функции cpu_percent() в пакете psutil получите загрузку CPU
            ram_value = psutil.virtual_memory().percent  # с помощью вызова функции virtual_memory().percent в пакете psutil получите загрузку RAM
            self.systemInfo_signal.emit([cpu_value, ram_value])  # с помощью метода .emit передайте в виде списка данные о загрузке CPU и RAM
            time.sleep(self.delay)  # с помощью функции .sleep() приостановите выполнение цикла на время self.delay


class WeatherHandler(QtCore.QThread):
    # Пропишите сигналы, которые считаете нужными
    weatherdataSignal = QtCore.Signal(dict)

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 10
        self.__status = None


    def setDelay(self, delay) -> None:
        """
        Метод для установки времени задержки обновления сайта

        :param delay: время задержки обновления информации о доступности сайта
        :return: None
        """

        self.__delay = delay

    def run(self) -> None:
        # TODO настройте метод для корректной работы

        while self.__status:
            # TODO Примерный код ниже

            response = requests.get(self.__api_url)
            data = response.json()
            self.weatherdataSignal.emit(data)
            time.sleep(self.__delay)

