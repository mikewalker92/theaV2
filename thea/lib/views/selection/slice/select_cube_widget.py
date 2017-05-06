from PySide import QtGui
from thea.lib.helpers.cube_utils import get_cube_names
from thea.lib.models.view_model import get_view_model
from thea.lib.views.thea_widget import TheaWidget


class SelectCubeWidget(TheaWidget):
    """
    A widget for selecting the cube to plot and changing the settings for the plot.
    """
    def __init__(self, view_model):
        """
        :type view_model: thea.lib.models.view_model.ViewModel
        """
        super(SelectCubeWidget, self).__init__()

        self._cube_selection_combo = QtGui.QComboBox()

        self._cube_options = view_model.options.cube_options

        self.init_ui()
        self.bind_events()

    def init_ui(self):
        self.setMaximumHeight(88)

        grid = QtGui.QGridLayout()

        grid.addWidget(QtGui.QLabel('Current Cube'), 0, 0)
        grid.addWidget(self._cube_selection_combo, 1, 0)

        self.setLayout(grid)

    def bind_events(self):
        self._cube_options.subscribe_update_function(self.update_cube_list)

    def update_cube_list(self):
        self._cube_selection_combo.clear()
        cube_names = get_cube_names(self._cube_options.cubes)
        self._cube_selection_combo.addItems(cube_names)


_select_cube_widget = SelectCubeWidget(
    get_view_model())


def get_select_cube_widget():
    """
    :rtype: SelectCubeWidget
    """
    return _select_cube_widget