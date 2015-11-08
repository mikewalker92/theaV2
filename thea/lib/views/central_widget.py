from PySide import QtGui
from PySide.QtCore import Qt
from thea.lib.views.cube_viewer_widget import CubeViewerWidget
from thea.lib.views.options_widget import OptionsWidget
from thea.lib.views.matplotlib_widget import MatplotlibWidget
from thea.lib.views.thea_widget import TheaWidget
from thea.resources.thea_colors import Colors


class CentralWidget(TheaWidget):
    """
    The CentralWidget divides the window into rough sections using splitters, and defines
    child widgets to populate the sections.
    """
    def __init__(self, renderer, matplotlib_widget, cube_viewer_widget, options_widget):
        super(CentralWidget, self).__init__(renderer)

        self._matplotlib_widget = matplotlib_widget
        self._cube_viewer_widget = cube_viewer_widget
        self._options_widget = options_widget

        self.init_ui()

    def init_ui(self):
        self.set_background_color(Colors.background_accent)

        splitter = QtGui.QSplitter(Qt.Vertical)
        splitter.addWidget(self._matplotlib_widget)
        splitter.addWidget(self._cube_viewer_widget)

        grid = QtGui.QGridLayout()
        grid.addWidget(splitter, 1, 0, 2, 1)
        grid.addWidget(self._options_widget, 1, 1, 2, 1)
        self.setLayout(grid)

        self.show_view()