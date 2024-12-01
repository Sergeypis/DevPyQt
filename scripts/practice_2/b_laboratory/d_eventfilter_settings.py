"""
Реализация программы взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings_form.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtCore, QtGui
from ui.d_eventfilter_settings_form import Ui_Form


class Window(QtWidgets.QWidget):
    key_press_signal = QtCore.Signal(int)
    lcd_load_signal = QtCore.Signal(int)
    settings = QtCore.QSettings('d_eventfilter_settings.ini', QtCore.QSettings.IniFormat)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.add_setupUi()

        self.initSignals()
        self.load_settings()

    def add_setupUi(self):
        """
        Доинициализация Ui

        :return: None
        """
        self.ui.dial.setMinimum(0)
        self.ui.dial.setMaximum(255)
        self.ui.dial.setSingleStep(1)
        self.ui.dial.setPageStep(15)
        self.ui.dial.setValue(0)
        self.ui.dial.setSliderPosition(0)
        self.ui.dial.setNotchTarget(15)
        self.ui.dial.setNotchesVisible(True)

        self.ui.horizontalSlider.setMinimum(0)
        self.ui.horizontalSlider.setMaximum(255)
        self.ui.horizontalSlider.setSingleStep(1)
        self.ui.horizontalSlider.setPageStep(15)
        self.ui.horizontalSlider.setValue(0)
        self.ui.horizontalSlider.setSliderPosition(0)
        self.ui.horizontalSlider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBothSides)
        self.ui.horizontalSlider.setTickInterval(15)

        self.ui.comboBox.setCurrentIndex(0)
        self.ui.comboBox.setCurrentText("Dec")
        self.ui.comboBox.addItems(["Dec", "Bin", "Oct", "Hex"])
        self.ui.comboBox.setEnabled(True)
        self.ui.comboBox.setModelColumn(0)

        self.ui.lcdNumber.setDigitCount(8)

    def load_settings(self) -> None:
        """
        Загрузка настроек в Ui

        :return: None
        """
        lcd_mode = self.settings.value("LCDmode", 0)
        lcd_value = self.settings.value("LCDvalue", 0)
        self.ui.comboBox.setCurrentIndex(int(lcd_mode))
        self.ui.lcdNumber.display(lcd_value)
        self.lcd_load_signal.emit(int(lcd_value))

    # events -----------------------------------------------------------
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        Перехват события нажатия кнопок клавиатуры, + и -
        Формирование сигнала key_press_signal с новым значением для QDial

        :param event: QtGui.QKeyEvent
        :return: None
        """
        curr_dial = self.ui.dial.value()
        if event.key() == QtCore.Qt.Key.Key_Plus:
            if curr_dial < self.ui.dial.maximum():
                self.key_press_signal.emit(curr_dial + 1)
        if event.key() == QtCore.Qt.Key.Key_Minus:
            if curr_dial > self.ui.dial.minimum():
                self.key_press_signal.emit(curr_dial - 1)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Событие закрытия окна

        :param event: QtGui.QCloseEvent
        :return: None
        """

        self.settings.setValue("LCDvalue", self.ui.lcdNumber.value())
        self.settings.setValue("LCDmode", self.ui.comboBox.currentIndex())

    # signals ----------------------------------------------------------
    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.ui.dial.valueChanged.connect(self.ui.lcdNumber.display)
        self.ui.horizontalSlider.sliderMoved.connect(self.ui.lcdNumber.display)
        self.ui.dial.sliderMoved.connect(self.ui.horizontalSlider.setValue)
        self.ui.horizontalSlider.valueChanged.connect(self.ui.dial.setValue)
        self.ui.comboBox.currentIndexChanged.connect(self.comboBoxChanged)
        self.key_press_signal.connect(self.ui.dial.setValue)
        self.lcd_load_signal.connect(self.ui.horizontalSlider.setValue)

    # slots --------------------------------------------------------------
    def comboBoxChanged(self) -> None:
        """
        Метод обрабатывающий изменение comboBox'a.
        Установка режима отображения QLCDNumber

        :return: None
        """
        send = self.sender()
        match send.currentIndex():
            case 0:
                self.ui.lcdNumber.setDecMode()
            case 1:
                self.ui.lcdNumber.setBinMode()
            case 2:
                self.ui.lcdNumber.setOctMode()
            case 3:
                self.ui.lcdNumber.setHexMode()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
