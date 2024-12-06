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
from PySide6 import QtWidgets,QtCore
from scripts.practice_3.b_laboratory.ui.sysinfo_widget import Ui_sys_info_form
from scripts.practice_3.b_laboratory.a_threads import SystemInfo


class SysWindow(QtWidgets.QWidget):
    # thread_delay_signal = QtCore.Signal(int)
    # lcd_load_signal = QtCore.Signal(int)
    # settings = QtCore.QSettings('d_eventfilter_settings.ini', QtCore.QSettings.IniFormat)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.thread_sys = None

        self.initThreads()
        self.ui_sys = Ui_sys_info_form()
        self.ui_sys.setupUi(self)
        self.add_setupUi()

        self.initSignals()
        self.load_settings()

    def add_setupUi(self):
        """
        Доинициализация Ui

        :return: None
        """

        self.move(self.screen().geometry().center().x() - 220 - self.width(), \
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

        self.thread_sys = SystemInfo()
        self.thread_sys.start()

    # settings -----------------------------------------------------------

    # events -----------------------------------------------------------

    # signals ----------------------------------------------------------
    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.ui_sys.dial_sys.valueChanged.connect(self.ui_sys.lcd_sys.display)
        self.ui_sys.dial_sys.sliderMoved.connect(self.ui_sys.spin_exactly.setValue)
        self.ui_sys.spin_exactly.valueChanged.connect(self.ui_sys.dial_sys.setValue)
        self.ui_sys.spin_exactly.valueChanged.connect(self.ui_sys.lcd_sys.display)

        self.ui_sys.spin_exactly.valueChanged.connect(self.change_sys_delay)
        self.thread_sys.systemInfo_signal.connect(self.set_system_indicator)

    # slots --------------------------------------------------------------

    def change_sys_delay(self, delay: float) -> None:
        self.thread_sys.thread_delay_signal.emit(delay)

    def set_system_indicator(self, sys_data: list):
        self.ui_sys.indicator_cpu.setValue(sys_data[0])
        self.ui_sys.indicator_ram.setValue(sys_data[1])

