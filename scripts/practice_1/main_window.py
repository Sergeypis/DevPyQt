from PySide6 import QtWidgets

from scripts.practice_1.ui.b_login import Ui_LoginForm
from scripts.practice_1.ui.c_ship_parameters import Ui_ShipForm
from scripts.practice_1.ui.d_engine import Ui_EngineForm
from scripts.practice_1.ui.e_profile_card import Ui_ProfileForm
from scripts.practice_1.ui.f_book_shop import Ui_BookShopForm
from scripts.practice_1.ui.g_calculator import Ui_CalcForm


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # self.ui = Ui_LoginForm()
        # self.ui.setupUi(self)Ui_ShipForm

        # self.ui = Ui_ShipForm()
        # self.ui.setupUi(self)

        # self.ui = Ui_EngineForm()
        # self.ui.setupUi(self)

        # self.ui = Ui_ProfileForm()
        # self.ui.setupUi(self)

        # self.ui = Ui_BookShopForm()
        # self.ui.setupUi(self)

        self.ui = Ui_CalcForm()
        self.ui.setupUi(self)

