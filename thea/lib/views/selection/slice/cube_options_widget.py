from PySide import QtGui

from thea.lib.views.selection.slice.major_axes_widget import get_major_axes_widget
from thea.lib.views.selection.slice.minor_axes_widget import get_minor_axes_widget
from thea.lib.views.selection.slice.select_cube_widget import get_select_cube_widget
from thea.lib.views.thea_widget import TheaWidget


class CubeOptionsWidget(TheaWidget):
    """
    A widget for selecting the cube to plot and changing the settings for the plot.
    """
    def __init__(self, select_cube_widget, major_axes_widget, minor_axes_widget):
        """
        :type select_cube_widget: thea.lib.views.select_cube_widget.SelectCubeWidget
        :type major_axes_widget: thea.lib.views.major_axes_widget.MajorAxesWidget
        :type minor_axes_widget: thea.lib.views.minor_axes_widget.MinorAxesWidget
        """
        super(CubeOptionsWidget, self).__init__()

        self._cubes_in_file = []
        self._cube_selection_combo = QtGui.QComboBox()

        self._select_cube_widget = select_cube_widget
        self._major_axes_widget = major_axes_widget
        self._minor_axes_widget = minor_axes_widget

        self.init_ui()

    def init_ui(self):
        grid = QtGui.QGridLayout()

        grid.addWidget(self._select_cube_widget, 0, 0)
        grid.addWidget(self._major_axes_widget, 1, 0)
        grid.addWidget(self._minor_axes_widget, 2, 0)

        self.setLayout(grid)


_cube_options_widget = CubeOptionsWidget(
    get_select_cube_widget(),
    get_major_axes_widget(),
    get_minor_axes_widget())


def get_cube_options_widget():
    return _cube_options_widget
