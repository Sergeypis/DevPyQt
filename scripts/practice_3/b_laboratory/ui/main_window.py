# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(440, 270)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(440, 270))
        MainWindow.setMaximumSize(QSize(440, 270))
        MainWindow.setBaseSize(QSize(0, 0))
        MainWindow.setAcceptDrops(True)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setStyleSheet(u"background-color: rgb(102, 102, 102);\n"
"color: rgb(255, 255, 0);")
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.exit_app_menu = QAction(MainWindow)
        self.exit_app_menu.setObjectName(u"exit_app_menu")
        self.exit_app_menu.setCheckable(False)
        self.exit_app_menu.setIconVisibleInMenu(True)
        self.exit_app_menu.setShortcutVisibleInContextMenu(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setSpacing(25)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(24, 25, 25, 25)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(25, 25, 25, 25)
        self.pb_open_sys_widget = QPushButton(self.groupBox)
        self.pb_open_sys_widget.setObjectName(u"pb_open_sys_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pb_open_sys_widget.sizePolicy().hasHeightForWidth())
        self.pb_open_sys_widget.setSizePolicy(sizePolicy1)
        self.pb_open_sys_widget.setStyleSheet(u"color: rgb(255, 170, 0);\n"
"font: 700 11pt \"Segoe UI\";\n"
"background-color: rgb(0, 170, 255);")

        self.horizontalLayout.addWidget(self.pb_open_sys_widget)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(25, 25, 25, 25)
        self.pb_open_weath_widget = QPushButton(self.groupBox_2)
        self.pb_open_weath_widget.setObjectName(u"pb_open_weath_widget")
        sizePolicy1.setHeightForWidth(self.pb_open_weath_widget.sizePolicy().hasHeightForWidth())
        self.pb_open_weath_widget.setSizePolicy(sizePolicy1)
        self.pb_open_weath_widget.setStyleSheet(u"color: rgb(255, 170, 0);\n"
"font: 700 11pt \"Segoe UI\";\n"
"background-color: rgb(0, 170, 255);")

        self.horizontalLayout_2.addWidget(self.pb_open_weath_widget)


        self.horizontalLayout_3.addWidget(self.groupBox_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 440, 22))
        self.menubar.setStyleSheet(u"background-color: rgb(88, 88, 88);")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"background-color: rgb(88, 88, 88);")
        self.menu.setTearOffEnabled(False)
        self.menu.setSeparatorsCollapsible(False)
        self.menu.setToolTipsVisible(False)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"background-color: rgb(108, 108, 108);\n"
"background-color: rgb(88, 88, 88);")
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.exit_app_menu)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0438 \u21163", None))
        self.exit_app_menu.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"SysInfo Widget", None))
        self.pb_open_sys_widget.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Weather Widget", None))
        self.pb_open_weath_widget.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
    # retranslateUi

