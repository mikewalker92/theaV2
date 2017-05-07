from PySide import QtGui
from PySide.QtGui import QComboBox, QLabel
from thea.bound.target import BoundComboBox
from thea.lib.helpers.view_helper_functions import get_axis_name
from thea.lib.models.view_model import get_view_model
from thea.lib.views.thea_widget import TheaWidget


class AxesWidget(TheaWidget):
    def __init__(self, cube_selection_model):
        """
        :type cube_selection_model: thea.lib.models.cube_selection_model.CubeSelectionModel
        """
        super(AxesWidget, self).__init__()

        self.__cube_selection_model = cube_selection_model

        self._x_axis_combo = BoundComboBox(cube_selection_model.x_axis, get_axis_name)
        self._y_axis_combo = BoundComboBox(cube_selection_model.y_axis, get_axis_name)

        self.init_ui()

    def init_ui(self):
        self.setMaximumHeight(110)

        grid = QtGui.QGridLayout()
        grid.addWidget(QLabel('Plot Axes'), 0, 0)
        grid.addWidget(self._x_axis_combo, 1, 0)
        grid.addWidget(self._y_axis_combo, 2, 0)

        self.setLayout(grid)


_major_axes_widget = AxesWidget(
    get_view_model().user_selection.cube_selection
)


def get_major_axes_widget():
    """
    :rtype: AxesWidget
    """
    return _major_axes_widget