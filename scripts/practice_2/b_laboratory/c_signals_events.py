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

from PySide6 import QtWidgets
from PySide6.QtGui import QGuiApplication
from ui.c_signals_events_form import Ui_Form


def get_time():
    return datetime.datetime.now().time().isoformat("seconds")


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

    # functions ------------------------------------------------------------
    def get_center_window(self) -> tuple:
        return self.geometry().center().x(), self.geometry().center().y()

    def get_pos_window(self) -> tuple:
        return self.pos().x(), self.pos().y()

    def min_size_window(self) -> tuple:
        return self.minimumSize().width(), self.minimumSize().height()

    def get_size_window(self) -> tuple:
        return self.geometry().width(), self.geometry().height()

    def get_current_screen(self) -> str:
        return self.screen().name()

    @staticmethod
    def get_primary_screen() -> str:
        return QGuiApplication.primaryScreen().name()

    def get_screen_resolution(self) -> tuple:
        return self.screen().geometry().width(), self.screen().geometry().height()

    @staticmethod
    def get_screen_count() -> int:
        return len(QGuiApplication.screens())

    # signals --------------------------------------------------------------
    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.ui.pushButtonGetData.clicked.connect(self.onPushButtonGetDataClicked)  # Сигнал нажатия на кнопку "Получить данные окна"

    # slots --------------------------------------------------------------
    def onPushButtonGetDataClicked(self):
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
        * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)

        :return: None
        """
        self.ui.plainTextEdit.setPlainText('\n'.join(self.get_screen_info_in_plainTextEdit()))

    def get_screen_info_in_plainTextEdit(self):
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
            f'==================================='
        ]
        return list_parametrs


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
