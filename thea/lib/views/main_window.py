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

    action_open = None

    def __init__(self, controller):
        super(MainWindow, self).__init__()

        self.controller = controller
        self.init_ui()
        self.set_up_actions()

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

        self.action_open = QtGui.QAction('&Open', self)

        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(self.action_open)
        file_menu.addAction(QtGui.QAction('&Save', self))
        file_menu.addAction(QtGui.QAction('&Exit', self))

    def set_up_actions(self):
        self.action_open.triggered.connect(self.open_file)

    def open_file(self):
        filename, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open File')

        self.controller.open_file(filename)
