# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'g_calculator.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_CalcForm(object):
    def setupUi(self, CalcForm):
        if not CalcForm.objectName():
            CalcForm.setObjectName(u"CalcForm")
        CalcForm.resize(934, 727)
        CalcForm.setMaximumSize(QSize(1500444, 16777215))
        self.verticalLayout = QVBoxLayout(CalcForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label = QLabel(CalcForm)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer = QSpacerItem(380, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(CalcForm)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(400, 0))
        font1 = QFont()
        font1.setPointSize(14)
        self.lineEdit.setFont(font1)
        self.lineEdit.setMaxLength(15)
        self.lineEdit.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.lineEdit, 0, Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_2 = QLabel(CalcForm)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(380, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.lineEdit_2 = QLineEdit(CalcForm)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)
        self.lineEdit_2.setMinimumSize(QSize(400, 0))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setMaxLength(15)
        self.lineEdit_2.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_2, 0, Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.pushButton = QPushButton(CalcForm)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignVCenter)

        self.pushButton_2 = QPushButton(CalcForm)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(CalcForm)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(CalcForm)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButton_4, 0, Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_3 = QLabel(CalcForm)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QSize(1500, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(85, 255, 127, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(85, 255, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        self.label_3.setPalette(palette)
        font2 = QFont()
        font2.setPointSize(72)
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.label_3.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.label_3.setTextFormat(Qt.TextFormat.AutoText)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.retranslateUi(CalcForm)
        self.lineEdit.textEdited.connect(self.label_3.setText)
        self.lineEdit_2.textEdited.connect(self.label_3.setText)

        QMetaObject.connectSlotsByName(CalcForm)
    # setupUi

    def retranslateUi(self, CalcForm):
        CalcForm.setWindowTitle(QCoreApplication.translate("CalcForm", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.label.setText(QCoreApplication.translate("CalcForm", u"\u041f\u0435\u0440\u0432\u043e\u0435 \u0447\u0438\u0441\u043b\u043e:", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("CalcForm", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0435\u0440\u0432\u043e\u0435 \u0447\u0438\u0441\u043b\u043e", None))
        self.label_2.setText(QCoreApplication.translate("CalcForm", u"\u0412\u0442\u043e\u0440\u043e\u0435 \u0447\u0438\u0441\u043b\u043e:", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("CalcForm", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0442\u043e\u0440\u043e\u0435 \u0447\u0438\u0441\u043b\u043e", None))
        self.pushButton.setText(QCoreApplication.translate("CalcForm", u"+", None))
        self.pushButton_2.setText(QCoreApplication.translate("CalcForm", u"-", None))
        self.pushButton_3.setText(QCoreApplication.translate("CalcForm", u"*", None))
        self.pushButton_4.setText(QCoreApplication.translate("CalcForm", u"/", None))
        self.label_3.setText(QCoreApplication.translate("CalcForm", u"0", None))
    # retranslateUi

