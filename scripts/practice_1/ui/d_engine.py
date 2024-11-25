# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'd_engine.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSlider, QSpacerItem, QVBoxLayout, QWidget)

class Ui_EngineForm(object):
    def setupUi(self, EngineForm):
        if not EngineForm.objectName():
            EngineForm.setObjectName(u"EngineForm")
        EngineForm.resize(1007, 244)
        self.horizontalLayout_2 = QHBoxLayout(EngineForm)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSlider_6 = QSlider(EngineForm)
        self.verticalSlider_6.setObjectName(u"verticalSlider_6")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalSlider_6.sizePolicy().hasHeightForWidth())
        self.verticalSlider_6.setSizePolicy(sizePolicy)
        self.verticalSlider_6.setMinimumSize(QSize(0, 200))
        self.verticalSlider_6.setMaximumSize(QSize(40, 16777215))
        self.verticalSlider_6.setOrientation(Qt.Vertical)
        self.verticalSlider_6.setInvertedAppearance(False)
        self.verticalSlider_6.setInvertedControls(False)
        self.verticalSlider_6.setTickPosition(QSlider.NoTicks)

        self.verticalLayout.addWidget(self.verticalSlider_6, 0, Qt.AlignHCenter)

        self.label = QLabel(EngineForm)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSlider_2 = QSlider(EngineForm)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        sizePolicy.setHeightForWidth(self.verticalSlider_2.sizePolicy().hasHeightForWidth())
        self.verticalSlider_2.setSizePolicy(sizePolicy)
        self.verticalSlider_2.setMinimumSize(QSize(0, 200))
        self.verticalSlider_2.setMaximumSize(QSize(40, 16777215))
        self.verticalSlider_2.setOrientation(Qt.Vertical)
        self.verticalSlider_2.setInvertedAppearance(False)
        self.verticalSlider_2.setInvertedControls(False)
        self.verticalSlider_2.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_2.addWidget(self.verticalSlider_2, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(EngineForm)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSlider_3 = QSlider(EngineForm)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        sizePolicy.setHeightForWidth(self.verticalSlider_3.sizePolicy().hasHeightForWidth())
        self.verticalSlider_3.setSizePolicy(sizePolicy)
        self.verticalSlider_3.setMinimumSize(QSize(0, 200))
        self.verticalSlider_3.setMaximumSize(QSize(40, 16777215))
        self.verticalSlider_3.setOrientation(Qt.Vertical)
        self.verticalSlider_3.setInvertedAppearance(False)
        self.verticalSlider_3.setInvertedControls(False)
        self.verticalSlider_3.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_3.addWidget(self.verticalSlider_3, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(EngineForm)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4, 0, Qt.AlignHCenter)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSlider_4 = QSlider(EngineForm)
        self.verticalSlider_4.setObjectName(u"verticalSlider_4")
        sizePolicy.setHeightForWidth(self.verticalSlider_4.sizePolicy().hasHeightForWidth())
        self.verticalSlider_4.setSizePolicy(sizePolicy)
        self.verticalSlider_4.setMinimumSize(QSize(0, 200))
        self.verticalSlider_4.setMaximumSize(QSize(40, 16777215))
        self.verticalSlider_4.setOrientation(Qt.Vertical)
        self.verticalSlider_4.setInvertedAppearance(False)
        self.verticalSlider_4.setInvertedControls(False)
        self.verticalSlider_4.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_4.addWidget(self.verticalSlider_4, 0, Qt.AlignHCenter)

        self.label_6 = QLabel(EngineForm)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6, 0, Qt.AlignHCenter)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSlider_5 = QSlider(EngineForm)
        self.verticalSlider_5.setObjectName(u"verticalSlider_5")
        self.verticalSlider_5.setEnabled(True)
        sizePolicy.setHeightForWidth(self.verticalSlider_5.sizePolicy().hasHeightForWidth())
        self.verticalSlider_5.setSizePolicy(sizePolicy)
        self.verticalSlider_5.setMinimumSize(QSize(0, 200))
        self.verticalSlider_5.setMaximumSize(QSize(40, 16777215))
        self.verticalSlider_5.setOrientation(Qt.Vertical)
        self.verticalSlider_5.setInvertedAppearance(False)
        self.verticalSlider_5.setInvertedControls(False)
        self.verticalSlider_5.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_5.addWidget(self.verticalSlider_5, 0, Qt.AlignHCenter)

        self.label_5 = QLabel(EngineForm)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5, 0, Qt.AlignHCenter)


        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(EngineForm)

        QMetaObject.connectSlotsByName(EngineForm)
    # setupUi

    def retranslateUi(self, EngineForm):
        EngineForm.setWindowTitle(QCoreApplication.translate("EngineForm", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u043c\u0438 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.label.setText(QCoreApplication.translate("EngineForm", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21161", None))
        self.label_2.setText(QCoreApplication.translate("EngineForm", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21162", None))
        self.label_4.setText(QCoreApplication.translate("EngineForm", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21163", None))
        self.label_6.setText(QCoreApplication.translate("EngineForm", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21164", None))
        self.label_5.setText(QCoreApplication.translate("EngineForm", u"\u041e\u0431\u0449\u0430\u044f \u0442\u044f\u0433\u0430", None))
    # retranslateUi

