# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'b_login.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        if not LoginForm.objectName():
            LoginForm.setObjectName(u"LoginForm")
        LoginForm.setWindowModality(Qt.NonModal)
        LoginForm.resize(400, 110)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginForm.sizePolicy().hasHeightForWidth())
        LoginForm.setSizePolicy(sizePolicy)
        LoginForm.setMinimumSize(QSize(400, 110))
        LoginForm.setMaximumSize(QSize(400, 110))
        self.verticalLayout_4 = QVBoxLayout(LoginForm)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.login_lbl = QLabel(LoginForm)
        self.login_lbl.setObjectName(u"login_lbl")
        sizePolicy.setHeightForWidth(self.login_lbl.sizePolicy().hasHeightForWidth())
        self.login_lbl.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.login_lbl.setFont(font)

        self.verticalLayout_2.addWidget(self.login_lbl)

        self.pass_lbl = QLabel(LoginForm)
        self.pass_lbl.setObjectName(u"pass_lbl")
        sizePolicy.setHeightForWidth(self.pass_lbl.sizePolicy().hasHeightForWidth())
        self.pass_lbl.setSizePolicy(sizePolicy)
        self.pass_lbl.setFont(font)

        self.verticalLayout_2.addWidget(self.pass_lbl)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.login_field = QLineEdit(LoginForm)
        self.login_field.setObjectName(u"login_field")

        self.verticalLayout.addWidget(self.login_field)

        self.pass_field = QLineEdit(LoginForm)
        self.pass_field.setObjectName(u"pass_field")

        self.verticalLayout.addWidget(self.pass_field)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.sign_in_btn = QPushButton(LoginForm)
        self.sign_in_btn.setObjectName(u"sign_in_btn")
        self.sign_in_btn.setFont(font)

        self.verticalLayout_3.addWidget(self.sign_in_btn)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.retranslateUi(LoginForm)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"\u0410\u0443\u0442\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f", None))
        self.login_lbl.setText(QCoreApplication.translate("LoginForm", u"Login", None))
        self.pass_lbl.setText(QCoreApplication.translate("LoginForm", u"Password", None))
        self.sign_in_btn.setText(QCoreApplication.translate("LoginForm", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

