"""
Реализация программы проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""
import datetime

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtGui import QGuiApplication
from ui.c_signals_events_form import Ui_Form


def get_time():
    return datetime.datetime.now().time().isoformat("seconds")


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()
        self.installEventFilter(self)

    # functions ------------------------------------------------------------
    def get_center_window(self) -> tuple:
        return self.geometry().center().x(), self.geometry().center().y()

    def get_pos_window(self) -> tuple:
        return self.pos().x(), self.pos().y()

    def min_size_window(self) -> tuple:
        return self.minimumSize().width(), self.minimumSize().height()

    def get_size_window(self) -> tuple:
        return self.frameSize().width(), self.frameSize().height()

    def get_current_screen(self) -> str:
        return self.screen().name()

    @staticmethod
    def get_primary_screen() -> str:
        return QGuiApplication.primaryScreen().name()

    def get_screen_resolution(self) -> tuple:
        return self.screen().geometry().width(), self.screen().geometry().height()

    def get_curr_scr_avaliable_geometry(self) -> QtCore.QRect:
        return self.screen().availableGeometry()

    @staticmethod
    def get_screen_count() -> int:
        return len(QGuiApplication.screens())

    # events -----------------------------------------------------------
    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        """
        Перехват события Resize, при изменении размера окна выводится его новый размер.

        :param watched: QtCore.QObject
        :param event: QtCore.QEvent
        :return: bool
        """

        # print(watched, event)

        if watched == self.window() and event.type() == QtCore.QEvent.Type.Resize:
            print(f'{get_time()} - Размер окна: {"x".join(map(str, self.get_size_window()))}')

        return super(Window, self).eventFilter(watched, event)

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        """
        Перехват события перемещения окна

        :param event: QtGui.QMoveEvent
        :return: None
        """

        print(f'{get_time()} - Старая позиция окна: {event.oldPos().toTuple()}')
        print(f'{get_time()} - Новая позиция окна: {event.pos().toTuple()}')
        print()
        QtWidgets.QWidget.moveEvent(self, event)

    def changeEvent(self, event: QtGui.QWindowStateChangeEvent) -> None:
        """
        Перехват события состояния окна:
        Свёрнуто, Развёрнуто, Активно, Полноэкранный режим

        :param event: QtGui.QWindowStateChangeEvent
        :return: None
        """
        if event.type() == 99:
            t = get_time()
            if self.isActiveWindow():
                print(f'{t} - "Oкнo активно"')

        # if self.isActiveWindow():
        #     print(event.type(), int(QtCore.QEvent.Type.WindowStateChange))
        #     t = get_time()
        #     print(f'{t} - "Oкнo активно"')

        if event.type() == QtCore.QEvent.Type.WindowStateChange:
            t = get_time()
            if self.isMinimized():
                print(f'{t} - "Oкнo свернуто"')
            elif self.isMaximized():
                print(f'{t} - "Окно развернуто"')
            elif self.isFullScreen():
                print(f'{t} - "Полноэкранный режим"')

            QtWidgets.QWidget.changeEvent(self, event)

    def showEvent(self, event: QtGui.QShowEvent) -> None:
        """
        Перехват события отображения окна

        :param event: QtGui.QShowEvent
        :return: None
        """
        print(f'{get_time()} - "Oкнo отображено"')
        QtWidgets.QWidget.showEvent(self, event)

    def hideEvent(self, event: QtGui.QHideEvent) -> None:
        """
        Перехват события скрытия окна

        :param event: QtGui.QHideEvent
        :return: None
        """
        print(f'{get_time()} - "Oкнo скрыто"')
        QtWidgets.QWidget.hideEvent(self, event)

    # signals --------------------------------------------------------------
    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.ui.pushButtonLT.clicked.connect(self.onPushButtonLTClicked)  # Сигнал нажатия на кновку "Переместить влево вверх"
        self.ui.pushButtonLB.clicked.connect(self.onPushButtonLBClicked)  # Сигнал нажатия на кновку "Переместить влево вниз"
        self.ui.pushButtonCenter.clicked.connect(self.onPushButtonCenterlicked)  # Сигнал нажатия на кновку "Переместить в центр"
        self.ui.pushButtonRT.clicked.connect(self.onPushButtonRTClicked)  # Сигнал нажатия на кновку "Переместить вправо вверх"
        self.ui.pushButtonRB.clicked.connect(self.onPushButtonRBClicked)  # Сигнал нажатия на кновку "Переместить вправо вниз"
        self.ui.pushButtonGetData.clicked.connect(self.onPushButtonGetDataClicked)  # Сигнал нажатия на кнопку "Получить данные окна"
        self.ui.pushButtonMoveCoords.clicked.connect(self.onPushButtonMoveCoordsClicked)  # Сигнал нажатия на кнопку "Переместить"

    # slots --------------------------------------------------------------

    def onPushButtonLTClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLT "Переместить влево вверх"

        :return: None
        """
        screen_geometry = self.get_curr_scr_avaliable_geometry()
        self.move(screen_geometry.x(), screen_geometry.y())

    def onPushButtonLBClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLB "Переместить влево вниз"

        :return: None
        """

        screen_geometry = self.get_curr_scr_avaliable_geometry()
        window_width, window_height = self.get_size_window()
        self.move(screen_geometry.x(), screen_geometry.height() - window_height + screen_geometry.y())

    def onPushButtonCenterlicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonCenter "Переместить в центр полезного экрана"

        :return: None
        """

        screen_center_point = self.get_curr_scr_avaliable_geometry().center()
        window_width, window_height = self.get_size_window()
        self.move(screen_center_point.x() - window_width//2, screen_center_point.y() - window_height//2)

    def onPushButtonRTClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonRT "Переместить вправо вверх"

        :return: None
        """
        screen_geometry = self.get_curr_scr_avaliable_geometry()
        window_width, window_height = self.get_size_window()
        self.move(screen_geometry.width() - window_width + screen_geometry.x(), screen_geometry.y())

    def onPushButtonRBClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonRB "Переместить вправо вниз"

        :return: None
        """
        screen_geometry = self.get_curr_scr_avaliable_geometry()
        window_width, window_height = self.get_size_window()
        self.move(screen_geometry.width() - window_width + screen_geometry.x(), screen_geometry.height() - window_height + screen_geometry.y())

    def onPushButtonMoveCoordsClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonMoveCoords "Переместить"

        :return: None
        """

        screen_geometry = self.get_curr_scr_avaliable_geometry()
        self.move(screen_geometry.x() + int(self.ui.spinBoxX.text()), screen_geometry.y() + int(self.ui.spinBoxY.text()))

    def onPushButtonGetDataClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonGetData
        Вывод информации в plainTextEdit:
        * Текущее время
        * Вывод кол-ва экранов
        * Текущее основное окно
        * Разрешение экрана
        * На каком экране окно находится
        * Размеры окна
        * Минимальные размеры окна
        * Текущее положение (координаты) окна
        * Координаты центра приложения

        :return: None
        """
        self.ui.plainTextEdit.setPlainText('\n'.join(self.get_screen_info_in_plainTextEdit()))

    def get_screen_info_in_plainTextEdit(self) -> list[str]:
        list_parametrs = [
            f'Текущее время: {get_time()}',
            f'Количество экранов: {self.get_screen_count()}',
            f'Текущее основное окно: {self.get_primary_screen()}',
            f'Текущий экран: {self.get_current_screen()}',
            f'Разрешение экрана: {"x".join(map(str, self.get_screen_resolution()))} px',
            f'Размеры окна ШхВ: {"x".join(map(str, self.get_size_window()))} px',
            f'Минимальные размеры окна ШхВ: {"x".join(map(str, self.min_size_window()))} px',
            f'Текущее положение (координаты) окна X*Y: {"x".join(map(str, self.get_pos_window()))} px',
            f'Координаты центра приложения X*Y: {"x".join(map(str, self.get_center_window()))} px',
            f'Координаты центра полезного экрана X*Y: {"x".join(map(str, self.get_curr_scr_avaliable_geometry().center().toTuple()))} px',
            f'===================================',
        ]
        return list_parametrs


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
