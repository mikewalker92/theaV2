from PySide import QtGui

from thea.lib.views.selection.slice.axes_widget import get_major_axes_widget
from thea.lib.views.selection.slice.minor_axes_widget import get_minor_axes_widget
from thea.lib.views.selection.slice.select_cube_widget import get_select_cube_widget
from thea.lib.views.thea_widget import TheaWidget
from thea.lib.views.selection.slice.select_cube_widget import SelectCubeWidget
from thea.lib.views.selection.slice.axes_widget import AxesWidget
from thea.lib.views.selection.slice.minor_axes_widget import CollapsedDimensionsWidget


class CubeOptionsWidget(TheaWidget):
    """
    A widget for selecting the cube to figure and changing the settings for the figure.
    """
    def __init__(self, select_cube_widget, major_axes_widget, minor_axes_widget):
        """
        :type select_cube_widget: SelectCubeWidget
        :type major_axes_widget: AxesWidget
        :type minor_axes_widget: CollapsedDimensionsWidget
        """
        super(CubeOptionsWidget, self).__init__()

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


__cube_options_widget = CubeOptionsWidget(
    select_cube_widget=get_select_cube_widget(),
    major_axes_widget=get_major_axes_widget(),
    minor_axes_widget=get_minor_axes_widget()
)


def get_cube_options_widget():
    return __cube_options_widget
