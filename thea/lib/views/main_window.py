from PySide.QtGui import QMenuBar
import matplotlib
from thea.resources.thea_colors import Colors

matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4'] = 'PySide'

import os
from PySide import QtGui
from thea.lib.views.central_widget import CentralWidget


class MainWindow(QtGui.QMainWindow):
    """
    This window is a container for the other UI elements. It also defines basic properties such as the
    title and the icon to be used by the operating system.
    """
    def __init__(self):
        super(MainWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.showMaximized()
        self.setWindowTitle('Thea')

        relative_path_to_icon = os.path.join(os.path.dirname(__file__), '../../resources/thea_icon.png')
        self.setWindowIcon(QtGui.QIcon(relative_path_to_icon))

        self.setCentralWidget(CentralWidget())

        self.init_menu()

        self.show()

    def init_menu(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(QtGui.QAction('&Open', self))
        file_menu.addAction(QtGui.QAction('&Save', self))
        file_menu.addAction(QtGui.QAction('&Exit', self))
