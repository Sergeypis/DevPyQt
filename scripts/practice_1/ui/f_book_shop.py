# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'f_book_shop.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_BookShopForm(object):
    def setupUi(self, BookShopForm):
        if not BookShopForm.objectName():
            BookShopForm.setObjectName(u"BookShopForm")
        BookShopForm.resize(500, 397)
        self.verticalLayout_3 = QVBoxLayout(BookShopForm)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(BookShopForm)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_3.addWidget(self.label)

        self.listWidget = QListWidget(BookShopForm)
        font1 = QFont()
        font1.setPointSize(11)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setFont(font1);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setFont(font1);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setFont(font1);
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_3.addWidget(self.listWidget)

        self.label_2 = QLabel(BookShopForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2)

        self.groupBox = QGroupBox(BookShopForm)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout.addWidget(self.radioButton_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.pushButton = QPushButton(BookShopForm)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 51))
        self.pushButton.setMaximumSize(QSize(16777215, 51))

        self.verticalLayout_3.addWidget(self.pushButton)


        self.retranslateUi(BookShopForm)

        QMetaObject.connectSlotsByName(BookShopForm)
    # setupUi

    def retranslateUi(self, BookShopForm):
        BookShopForm.setWindowTitle(QCoreApplication.translate("BookShopForm", u"\u0412\u044b\u0431\u043e\u0440 \u043a\u043d\u0438\u0433\u0438 \u0434\u043b\u044f \u043f\u043e\u043a\u0443\u043f\u043a\u0438", None))
        self.label.setText(QCoreApplication.translate("BookShopForm", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u043d\u0438\u0433\u0443", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("BookShopForm", u"\u0413\u0430\u0440\u0440\u0438 \u043f\u043e\u0442\u0442\u0435\u0440 \u0438 \u0443\u0437\u043d\u0438\u043a \u0410\u0437\u043a\u0430\u0431\u0430\u043d\u0430 \u0414\u0436\u043e\u0430\u043d \u0420\u043e\u0443\u043b\u0438\u043d\u0433", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("BookShopForm", u"\u0411\u043b\u0430\u0433\u043e\u0441\u043b\u043e\u0432\u0435\u043d\u0438\u0435 \u043d\u0435\u0431\u043e\u0436\u0438\u0442\u0435\u043b\u0435\u0439. \u0422\u043e\u043c 3 \u041c\u043e\u0441\u044f\u043d \u0422\u0443\u043d\u0441\u044e", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("BookShopForm", u"\u0423\u043d\u0435\u0441\u0451\u043d\u043d\u044b\u0435 \u0432\u0435\u0442\u0440\u043e\u043c \u041c\u0430\u0440\u0433\u0430\u0440\u0435\u0442 \u041c\u0438\u0442\u0447\u0435\u043b\u043b", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label_2.setText(QCoreApplication.translate("BookShopForm", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043f\u043e\u0441\u043e\u0431 \u043e\u043f\u043b\u0430\u0442\u044b", None))
        self.groupBox.setTitle("")
        self.radioButton.setText(QCoreApplication.translate("BookShopForm", u"\u041f\u043e \u043a\u0430\u0440\u0442\u0435", None))
        self.radioButton_2.setText(QCoreApplication.translate("BookShopForm", u"\u041f\u043e QR", None))
        self.radioButton_3.setText(QCoreApplication.translate("BookShopForm", u"\u041d\u0430\u043b\u0438\u0447\u043d\u044b\u043c\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("BookShopForm", u"\u041e\u043f\u043b\u0430\u0442\u0438\u0442\u044c", None))
    # retranslateUi

