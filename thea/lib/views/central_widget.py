from PySide import QtGui
from PySide.QtCore import Qt

from thea.lib.views.details.cube_viewer_widget import get_cube_viewer_widget, CubeViewerWidget
from thea.lib.views.figure.matplotlib_widget import get_matplotlib_widget, MatplotlibWidget
from thea.lib.views.selection.user_selection_widget import create_user_selection_widget, UserSelectionWidget
from thea.lib.views.thea_widget import TheaWidget
from thea.resources.thea_colors import Colors


class CentralWidget(TheaWidget):
    """
    The CentralWidget divides the window into rough sections using splitters, and defines
    child widgets to populate the sections.
    """
    def __init__(self, matplotlib_widget, cube_viewer_widget, user_selection_widget):
        """
        :type matplotlib_widget: MatplotlibWidget
        :type cube_viewer_widget: CubeViewerWidget
        :type user_selection_widget: UserSelectionWidget
        """
        super(CentralWidget, self).__init__()

        self._matplotlib_widget = matplotlib_widget
        self._cube_viewer_widget = cube_viewer_widget
        self._user_selection_widget = user_selection_widget

        self.init_ui()

    def init_ui(self):
        self.set_background_color(Colors.background_accent)

        splitter = QtGui.QSplitter(Qt.Vertical)
        splitter.addWidget(self._matplotlib_widget)
        splitter.addWidget(self._cube_viewer_widget)

        grid = QtGui.QGridLayout()
        grid.addWidget(splitter, 1, 0, 2, 1)
        grid.addWidget(self._user_selection_widget, 1, 1, 2, 1)
        self.setLayout(grid)


def create_central_widget():
    """
    :rtype: CentralWidget
    """
    return CentralWidget(
        matplotlib_widget=get_matplotlib_widget(),
        cube_viewer_widget=get_cube_viewer_widget(),
        user_selection_widget=create_user_selection_widget()
    )