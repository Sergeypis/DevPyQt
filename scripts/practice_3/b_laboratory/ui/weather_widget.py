# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weather_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_weather_form(object):
    def setupUi(self, weather_form):
        if not weather_form.objectName():
            weather_form.setObjectName(u"weather_form")
        weather_form.setWindowModality(Qt.WindowModality.WindowModal)
        weather_form.resize(310, 355)
        weather_form.setStyleSheet(u"background-color: rgb(102, 102, 102);\n"
"color: rgb(255, 255, 0);")
        self.verticalLayout_5 = QVBoxLayout(weather_form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_weather_widget = QLabel(weather_form)
        self.lbl_weather_widget.setObjectName(u"lbl_weather_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_weather_widget.sizePolicy().hasHeightForWidth())
        self.lbl_weather_widget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbl_weather_widget.setFont(font)
        self.lbl_weather_widget.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.lbl_weather_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.lbl_weather_widget)

        self.widget_weather = QWidget(weather_form)
        self.widget_weather.setObjectName(u"widget_weather")
        self.verticalLayout_4 = QVBoxLayout(self.widget_weather)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gb_delay_sys = QGroupBox(self.widget_weather)
        self.gb_delay_sys.setObjectName(u"gb_delay_sys")
        sizePolicy.setHeightForWidth(self.gb_delay_sys.sizePolicy().hasHeightForWidth())
        self.gb_delay_sys.setSizePolicy(sizePolicy)
        self.gb_delay_sys.setAutoFillBackground(False)
        self.gb_delay_sys.setStyleSheet(u"color: rgb(255, 255, 0);\n"
"alternate-background-color: rgb(255, 255, 0);")
        self.gb_delay_sys.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_3 = QVBoxLayout(self.gb_delay_sys)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.gb_delay_sys)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.input_delay = QLineEdit(self.gb_delay_sys)
        self.input_delay.setObjectName(u"input_delay")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input_delay.sizePolicy().hasHeightForWidth())
        self.input_delay.setSizePolicy(sizePolicy1)
        self.input_delay.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.input_delay.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.input_delay.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.input_delay.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.input_delay)

        self.cb_units_duration = QComboBox(self.gb_delay_sys)
        self.cb_units_duration.addItem("")
        self.cb_units_duration.addItem("")
        self.cb_units_duration.addItem("")
        self.cb_units_duration.setObjectName(u"cb_units_duration")
        sizePolicy1.setHeightForWidth(self.cb_units_duration.sizePolicy().hasHeightForWidth())
        self.cb_units_duration.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.cb_units_duration)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addWidget(self.gb_delay_sys)

        self.gb_info_sys = QGroupBox(self.widget_weather)
        self.gb_info_sys.setObjectName(u"gb_info_sys")
        sizePolicy.setHeightForWidth(self.gb_info_sys.sizePolicy().hasHeightForWidth())
        self.gb_info_sys.setSizePolicy(sizePolicy)
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
        self.input_lat = QLineEdit(self.gb_info_sys)
        self.input_lat.setObjectName(u"input_lat")
        self.input_lat.setEchoMode(QLineEdit.EchoMode.Normal)

        self.verticalLayout.addWidget(self.input_lat)

        self.input_lon_2 = QLineEdit(self.gb_info_sys)
        self.input_lon_2.setObjectName(u"input_lon_2")

        self.verticalLayout.addWidget(self.input_lon_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_4.addWidget(self.gb_info_sys)

        self.output_field = QPlainTextEdit(self.widget_weather)
        self.output_field.setObjectName(u"output_field")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.output_field.sizePolicy().hasHeightForWidth())
        self.output_field.setSizePolicy(sizePolicy2)
        self.output_field.setMinimumSize(QSize(0, 50))
        self.output_field.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.output_field)

        self.pb_get_data = QPushButton(self.widget_weather)
        self.pb_get_data.setObjectName(u"pb_get_data")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pb_get_data.sizePolicy().hasHeightForWidth())
        self.pb_get_data.setSizePolicy(sizePolicy3)

        self.verticalLayout_4.addWidget(self.pb_get_data, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_5.addWidget(self.widget_weather)


        self.retranslateUi(weather_form)

        QMetaObject.connectSlotsByName(weather_form)
    # setupUi

    def retranslateUi(self, weather_form):
        weather_form.setWindowTitle(QCoreApplication.translate("weather_form", u"Weather API", None))
        self.lbl_weather_widget.setText(QCoreApplication.translate("weather_form", u"WeatherWidget", None))
        self.gb_delay_sys.setTitle(QCoreApplication.translate("weather_form", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043f\u0435\u0440\u0438\u043e\u0434\u0430 \u043e\u043f\u0440\u043e\u0441\u0430", None))
        self.label.setText(QCoreApplication.translate("weather_form", u"\u0412\u0435\u0435\u0434\u0438\u0442\u0435 \u0447\u0438\u0441\u043b\u043e:", None))
        self.input_delay.setText(QCoreApplication.translate("weather_form", u"1", None))
        self.cb_units_duration.setItemText(0, QCoreApplication.translate("weather_form", u"\u0441\u0435\u043a", None))
        self.cb_units_duration.setItemText(1, QCoreApplication.translate("weather_form", u"\u043c\u0438\u043d", None))
        self.cb_units_duration.setItemText(2, QCoreApplication.translate("weather_form", u"\u0447\u0430\u0441", None))

        self.gb_info_sys.setTitle(QCoreApplication.translate("weather_form", u"\u0412\u0432\u043e\u0434 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442", None))
        self.lbl_cpu.setText(QCoreApplication.translate("weather_form", u"\u0428\u0438\u0440\u043e\u0442\u0430:", None))
        self.lbl_ram.setText(QCoreApplication.translate("weather_form", u"\u0414\u043e\u043b\u0433\u043e\u0442\u0430:", None))
        self.input_lat.setText(QCoreApplication.translate("weather_form", u"59.687839", None))
        self.input_lat.setPlaceholderText(QCoreApplication.translate("weather_form", u"59.687839", None))
        self.input_lon_2.setText(QCoreApplication.translate("weather_form", u"30.407833", None))
        self.input_lon_2.setPlaceholderText(QCoreApplication.translate("weather_form", u"30.407833", None))
        self.pb_get_data.setText(QCoreApplication.translate("weather_form", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
    # retranslateUi

