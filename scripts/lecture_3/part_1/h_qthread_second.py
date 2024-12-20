"""
Использование потока через класс наследованный от QThread
"""

import time

from PySide6 import QtCore, QtWidgets


class Worker(QtCore.QThread):
    progress = QtCore.Signal(int)

    def run(self) -> None:
        """
        Метод имитирующий долгую задачу

        :return: None
        """

        for i in range(5):
            time.sleep(1)
            self.progress.emit(i + 1)


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThreads()
        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.label = QtWidgets.QLabel("Выполнение долгой задачи: ")
        self.pushButton = QtWidgets.QPushButton("Запустить долгую задачу")
        self.pushButtonOtherProcess = QtWidgets.QPushButton("Другие действия с GUI")
        self.plainTextEdit = QtWidgets.QPlainTextEdit()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.pushButton)
        layout.addWidget(self.pushButtonOtherProcess)
        layout.addWidget(self.plainTextEdit)

        self.setLayout(layout)

    def initThreads(self) -> None:
        """
        Инициализация потоков

        :return: None
        """

        self.thread = Worker()

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButton.clicked.connect(self.runLongProcess)
        self.pushButtonOtherProcess.clicked.connect(
            lambda: self.plainTextEdit.appendPlainText(f"{time.ctime()}: push clicked")
        )

        self.thread.started.connect(lambda: print("Thread started"))
        self.thread.progress.connect(self.reportProgress)
        self.thread.finished.connect(lambda: self.pushButton.setEnabled(True))


    def runLongProcess(self) -> None:
        """
        Запуск потока с "долгим" выполнением

        :return: None
        """

        self.pushButton.setEnabled(False)
        self.thread.start()

    def reportProgress(self, progress) -> None:
        """
        Приём данных из потока и обработка их в основном цикле приложения

        :param progress: прогресс выполнения функции в потоке
        :return: None
        """

        self.label.setText(f"Выполнение долгой задачи: {progress}")

if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
