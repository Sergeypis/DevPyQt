# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'e_profile_card.ui'
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

class Ui_ProfileForm(object):
    def setupUi(self, ProfileForm):
        if not ProfileForm.objectName():
            ProfileForm.setObjectName(u"ProfileForm")
        ProfileForm.resize(750, 170)
        ProfileForm.setWindowTitle("Карточка пользователя")
        ProfileForm.setMinimumSize(QSize(750, 170))
        ProfileForm.setMaximumSize(QSize(750, 170))
        self.horizontalLayout = QHBoxLayout(ProfileForm)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, -1, -1)
        self.label = QLabel(ProfileForm)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(ProfileForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(ProfileForm)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(ProfileForm)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_2.addWidget(self.label_4)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, -1, -1)
        self.lineEdit = QLineEdit(ProfileForm)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 31))
        self.lineEdit.setMaximumSize(QSize(16777215, 31))
        font1 = QFont()
        font1.setPointSize(11)
        self.lineEdit.setFont(font1)

        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(ProfileForm)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 31))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_2.setFont(font1)

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(ProfileForm)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 31))
        self.lineEdit_3.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_3.setFont(font1)

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(ProfileForm)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 31))
        self.lineEdit_4.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_4.setFont(font1)

        self.verticalLayout.addWidget(self.lineEdit_4)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(ProfileForm)

        QMetaObject.connectSlotsByName(ProfileForm)
    # setupUi

    def retranslateUi(self, ProfileForm):
        #ProfileForm.setWindowTitle(QCoreApplication.translate("ProfileForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("ProfileForm", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("ProfileForm", u"\u0418\u043c\u044f", None))
        self.label_3.setText(QCoreApplication.translate("ProfileForm", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_4.setText(QCoreApplication.translate("ProfileForm", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("ProfileForm", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0443 \u0444\u0430\u043c\u0438\u043b\u0438\u044e", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("ProfileForm", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0435 \u0438\u043c\u044f", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("ProfileForm", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0435 \u043e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("ProfileForm", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448 \u0442\u0435\u043b\u0435\u0444\u043e\u043d", None))
    # retranslateUi

