# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sysinfo_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QDial, QDoubleSpinBox, QGroupBox,
    QHBoxLayout, QLCDNumber, QLabel, QProgressBar,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_sys_info_form(object):
    def setupUi(self, sys_info_form):
        if not sys_info_form.objectName():
            sys_info_form.setObjectName(u"sys_info_form")
        sys_info_form.resize(310, 355)
        sys_info_form.setStyleSheet(u"background-color: rgb(102, 102, 102);\n"
"color: rgb(255, 255, 0);")
        self.verticalLayout_6 = QVBoxLayout(sys_info_form)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_sys_widget = QLabel(sys_info_form)
        self.lbl_sys_widget.setObjectName(u"lbl_sys_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_sys_widget.sizePolicy().hasHeightForWidth())
        self.lbl_sys_widget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbl_sys_widget.setFont(font)
        self.lbl_sys_widget.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.lbl_sys_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.lbl_sys_widget)

        self.widget_system = QWidget(sys_info_form)
        self.widget_system.setObjectName(u"widget_system")
        self.horizontalLayout = QHBoxLayout(self.widget_system)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gb_delay_sys = QGroupBox(self.widget_system)
        self.gb_delay_sys.setObjectName(u"gb_delay_sys")
        self.gb_delay_sys.setAutoFillBackground(False)
        self.gb_delay_sys.setStyleSheet(u"color: rgb(255, 255, 0);\n"
"alternate-background-color: rgb(255, 255, 0);")
        self.gb_delay_sys.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_6 = QHBoxLayout(self.gb_delay_sys)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_rough = QLabel(self.gb_delay_sys)
        self.lbl_rough.setObjectName(u"lbl_rough")
        sizePolicy.setHeightForWidth(self.lbl_rough.sizePolicy().hasHeightForWidth())
        self.lbl_rough.setSizePolicy(sizePolicy)
        self.lbl_rough.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_rough)

        self.dial_sys = QDial(self.gb_delay_sys)
        self.dial_sys.setObjectName(u"dial_sys")
        self.dial_sys.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.dial_sys.setMinimum(1)
        self.dial_sys.setMaximum(5)
        self.dial_sys.setSingleStep(1)
        self.dial_sys.setPageStep(1)
        self.dial_sys.setWrapping(False)
        self.dial_sys.setNotchTarget(5.000000000000000)
        self.dial_sys.setNotchesVisible(True)

        self.verticalLayout_3.addWidget(self.dial_sys)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_1sec = QLabel(self.gb_delay_sys)
        self.lbl_1sec.setObjectName(u"lbl_1sec")
        sizePolicy.setHeightForWidth(self.lbl_1sec.sizePolicy().hasHeightForWidth())
        self.lbl_1sec.setSizePolicy(sizePolicy)
        self.lbl_1sec.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lbl_1sec)

        self.lbl_5sec = QLabel(self.gb_delay_sys)
        self.lbl_5sec.setObjectName(u"lbl_5sec")
        sizePolicy.setHeightForWidth(self.lbl_5sec.sizePolicy().hasHeightForWidth())
        self.lbl_5sec.setSizePolicy(sizePolicy)
        self.lbl_5sec.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lbl_5sec)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_exactly = QLabel(self.gb_delay_sys)
        self.lbl_exactly.setObjectName(u"lbl_exactly")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_exactly.sizePolicy().hasHeightForWidth())
        self.lbl_exactly.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.lbl_exactly)

        self.spin_exactly = QDoubleSpinBox(self.gb_delay_sys)
        self.spin_exactly.setObjectName(u"spin_exactly")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spin_exactly.sizePolicy().hasHeightForWidth())
        self.spin_exactly.setSizePolicy(sizePolicy2)
        self.spin_exactly.setStyleSheet(u"color: rgb(255, 170, 0);\n"
"background-color: rgb(74, 74, 74);\n"
"")
        self.spin_exactly.setDecimals(3)
        self.spin_exactly.setMinimum(0.100000000000000)
        self.spin_exactly.setMaximum(5.000000000000000)
        self.spin_exactly.setSingleStep(0.005000000000000)
        self.spin_exactly.setValue(1.000000000000000)

        self.horizontalLayout_3.addWidget(self.spin_exactly)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.lcd_sys = QLCDNumber(self.gb_delay_sys)
        self.lcd_sys.setObjectName(u"lcd_sys")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lcd_sys.sizePolicy().hasHeightForWidth())
        self.lcd_sys.setSizePolicy(sizePolicy3)
        self.lcd_sys.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lcd_sys.setAutoFillBackground(False)
        self.lcd_sys.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 0, 0);")
        self.lcd_sys.setSmallDecimalPoint(True)
        self.lcd_sys.setDigitCount(3)
        self.lcd_sys.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.lcd_sys.setProperty("value", 0.000000000000000)

        self.horizontalLayout_6.addWidget(self.lcd_sys)


        self.verticalLayout_4.addWidget(self.gb_delay_sys)

        self.gb_info_sys = QGroupBox(self.widget_system)
        self.gb_info_sys.setObjectName(u"gb_info_sys")
        self.gb_info_sys.setStyleSheet(u"color: rgb(255, 255, 0);")
        self.gb_info_sys.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_2 = QHBoxLayout(self.gb_info_sys)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_cpu = QLabel(self.gb_info_sys)
        self.lbl_cpu.setObjectName(u"lbl_cpu")

        self.verticalLayout_2.addWidget(self.lbl_cpu)

        self.lbl_ram = QLabel(self.gb_info_sys)
        self.lbl_ram.setObjectName(u"lbl_ram")

        self.verticalLayout_2.addWidget(self.lbl_ram)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.indicator_cpu = QProgressBar(self.gb_info_sys)
        self.indicator_cpu.setObjectName(u"indicator_cpu")
        self.indicator_cpu.setValue(24)
        self.indicator_cpu.setTextVisible(True)
        self.indicator_cpu.setOrientation(Qt.Orientation.Horizontal)
        self.indicator_cpu.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.verticalLayout.addWidget(self.indicator_cpu)

        self.indicator_ram = QProgressBar(self.gb_info_sys)
        self.indicator_ram.setObjectName(u"indicator_ram")
        self.indicator_ram.setValue(24)

        self.verticalLayout.addWidget(self.indicator_ram)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_4.addWidget(self.gb_info_sys)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addWidget(self.widget_system)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.retranslateUi(sys_info_form)

        QMetaObject.connectSlotsByName(sys_info_form)
    # setupUi

    def retranslateUi(self, sys_info_form):
        sys_info_form.setWindowTitle(QCoreApplication.translate("sys_info_form", u"System Info", None))
        self.lbl_sys_widget.setText(QCoreApplication.translate("sys_info_form", u"SystemInfo Widget", None))
        self.gb_delay_sys.setTitle(QCoreApplication.translate("sys_info_form", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0438", None))
        self.lbl_rough.setText(QCoreApplication.translate("sys_info_form", u"\u0413\u0440\u0443\u0431\u043e:", None))
        self.lbl_1sec.setText(QCoreApplication.translate("sys_info_form", u"1\u0441", None))
        self.lbl_5sec.setText(QCoreApplication.translate("sys_info_form", u"5\u0441", None))
        self.lbl_exactly.setText(QCoreApplication.translate("sys_info_form", u"\u0422\u043e\u0447\u043d\u043e:", None))
        self.gb_info_sys.setTitle(QCoreApplication.translate("sys_info_form", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0441\u0438\u0441\u0442\u0435\u043c\u0435", None))
        self.lbl_cpu.setText(QCoreApplication.translate("sys_info_form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 CPU", None))
        self.lbl_ram.setText(QCoreApplication.translate("sys_info_form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 RAM", None))
    # retranslateUi

