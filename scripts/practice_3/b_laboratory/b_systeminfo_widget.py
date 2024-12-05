"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
from PySide6 import QtWidgets
from scripts.practice_3.b_laboratory.ui.sysinfo_widget import Ui_sys_info_form


class Window(QtWidgets.QWidget):
    # key_press_signal = QtCore.Signal(int)
    # lcd_load_signal = QtCore.Signal(int)
    # settings = QtCore.QSettings('d_eventfilter_settings.ini', QtCore.QSettings.IniFormat)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_sys_info_form()
        self.ui.setupUi(self)
        self.add_setupUi()

        self.initSignals()
        self.load_settings()

    def add_setupUi(self):
        """
        Доинициализация Ui

        :return: None
        """
        pass

    def load_settings(self) -> None:
        """
        Загрузка настроек в Ui

        :return: None
        """
        pass

    # settings -----------------------------------------------------------

    # events -----------------------------------------------------------

    # signals ----------------------------------------------------------
    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        pass

    # slots --------------------------------------------------------------


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()