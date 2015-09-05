from PySide import QtGui
from PySide.QtCore import Qt
from thea.lib.views.cube_viewer_widget import CubeViewerWidget
from thea.lib.views.options_widget import OptionsWidget
from thea.lib.views.matplotlib_widget import MatplotlibWidget
from thea.lib.views.thea_widgets import TheaWidget
from thea.resources.thea_colors import Colors


class CentralWidget(TheaWidget):
    """
    The CentralWidget divides the window into rough sections using splitters, and defines
    child widgets to populate the sections.
    """
    def __init__(self):
        super(CentralWidget, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.set_background_color(Colors.background_accent)

        splitter = QtGui.QSplitter(Qt.Vertical)
        splitter.addWidget(MatplotlibWidget())
        splitter.addWidget(CubeViewerWidget())

        grid = QtGui.QGridLayout()
        grid.addWidget(splitter, 1, 0, 2, 1)
        grid.addWidget(OptionsWidget(), 1, 1, 2, 1)
        self.setLayout(grid)

        self.show()