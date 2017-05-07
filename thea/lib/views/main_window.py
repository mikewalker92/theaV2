import os
from PySide import QtGui
from thea.lib.controllers.new_cube_controller import get_new_cube_controller, NewCubeController
from thea.lib.views.central_widget import create_central_widget, CentralWidget


class MainWindow(QtGui.QMainWindow):
    """
    This window is a container for the other UI elements. It also defines basic properties such as the
    title and the icon to be used by the operating system.
    """

    action_open = None

    def __init__(self, central_widget, new_cube_controller):
        """
        :type central_widget: CentralWidget
        :type new_cube_controller: NewCubeController
        """
        super(MainWindow, self).__init__()

        self._central_widget = central_widget
        self._new_cube_controller = new_cube_controller

        self.init_ui()
        self.set_up_actions()

    def init_ui(self):
        self.showMaximized()
        self.setWindowTitle('Thea')

        relative_path_to_icon = os.path.join(os.path.dirname(__file__), '../../resources/thea_icon.png')
        self.setWindowIcon(QtGui.QIcon(relative_path_to_icon))

        self.setCentralWidget(self._central_widget)

        self.init_menu()

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
        self._new_cube_controller.open_file(filename)


_main_window = MainWindow(
    create_central_widget(),
    get_new_cube_controller())


def get_main_window():
    """
    :rtype: MainWindow
    """
    return _main_window