from PySide import QtGui

from thea.lib.views.selection.slice.axes_widget import get_major_axes_widget
from thea.lib.views.selection.slice.collapsed_dimensions_widget import get_collapsed_dimensions_widget
from thea.lib.views.selection.slice.select_cube_widget import get_select_cube_widget
from thea.lib.views.thea_widget import TheaWidget
from thea.lib.views.selection.slice.select_cube_widget import SelectCubeWidget
from thea.lib.views.selection.slice.axes_widget import AxesWidget
from thea.lib.views.selection.slice.collapsed_dimensions_widget import CollapsedDimensionsWidget


class SliceSelectionWidget(TheaWidget):
    """
    A widget for selecting the cube to figure and changing the settings for the figure.
    """
    def __init__(self, select_cube_widget, axes_widget, collapsed_dimensions_widget):
        """
        :type select_cube_widget: SelectCubeWidget
        :type axes_widget: AxesWidget
        :type collapsed_dimensions_widget: CollapsedDimensionsWidget
        """
        super(SliceSelectionWidget, self).__init__()

        self._select_cube_widget = select_cube_widget
        self._axes_widget = axes_widget
        self._collapsed_dimensions_widget = collapsed_dimensions_widget

        self.init_ui()

    def init_ui(self):
        grid = QtGui.QGridLayout()

        grid.addWidget(self._select_cube_widget, 0, 0)
        grid.addWidget(self._axes_widget, 1, 0)
        grid.addWidget(self._collapsed_dimensions_widget, 2, 0)

        self.setLayout(grid)


def get_slice_selection_widget():
    return SliceSelectionWidget(
        select_cube_widget=get_select_cube_widget(),
        axes_widget=get_major_axes_widget(),
        collapsed_dimensions_widget=get_collapsed_dimensions_widget()
    )
