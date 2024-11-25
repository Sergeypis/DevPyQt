# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'c_ship_parameters.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ShipForm(object):
    def setupUi(self, ShipForm):
        if not ShipForm.objectName():
            ShipForm.setObjectName(u"ShipForm")
        ShipForm.resize(340, 154)
        self.horizontalLayout = QHBoxLayout(ShipForm)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(ShipForm)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(ShipForm)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(ShipForm)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(ShipForm)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(ShipForm)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(ShipForm)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(ShipForm)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(ShipForm)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(ShipForm)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(ShipForm)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout.addWidget(self.lineEdit_5)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(ShipForm)

        QMetaObject.connectSlotsByName(ShipForm)
    # setupUi

    def retranslateUi(self, ShipForm):
        ShipForm.setWindowTitle(QCoreApplication.translate("ShipForm", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043e\u0440\u0430\u0431\u043b\u044f", None))
        self.label.setText(QCoreApplication.translate("ShipForm", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043d\u0430 \u0431\u043e\u0440\u0442\u0443", None))
        self.label_2.setText(QCoreApplication.translate("ShipForm", u"\u0420\u0430\u0437\u0433\u0435\u0440\u043c\u0435\u0442\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("ShipForm", u"\u0411\u0430\u043a \u21161", None))
        self.label_4.setText(QCoreApplication.translate("ShipForm", u"\u0411\u0430\u043a \u21162", None))
        self.label_5.setText(QCoreApplication.translate("ShipForm", u"\u0411\u0430\u043a \u21163", None))
        self.lineEdit.setText(QCoreApplication.translate("ShipForm", u"22 C", None))
        self.lineEdit_2.setText(QCoreApplication.translate("ShipForm", u"\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.lineEdit_3.setText(QCoreApplication.translate("ShipForm", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.lineEdit_4.setText(QCoreApplication.translate("ShipForm", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.lineEdit_5.setText(QCoreApplication.translate("ShipForm", u"\u041d\u043e\u0440\u043c\u0430", None))
    # retranslateUi

