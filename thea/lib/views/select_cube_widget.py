from PySide import QtGui
from thea.lib.helpers.cube_utils import get_names_from_cubes
from thea.lib.models.cube_selection_model import get_cube_selection_model
from thea.lib.views.thea_widget import TheaWidget


class SelectCubeWidget(TheaWidget):
    """
    A widget for selecting the cube to plot and changing the settings for the plot.
    """
    def __init__(self, cube_selection_model):
        super(SelectCubeWidget, self).__init__()

        self._cubes_in_file = []
        self._cube_selection_combo = QtGui.QComboBox()

        self._cube_selection_model = cube_selection_model

        self.init_ui()
        self.bind_events()

    def init_ui(self):
        self.setMaximumHeight(88)

        grid = QtGui.QGridLayout()

        grid.addWidget(QtGui.QLabel('Current Cube'), 0, 0)
        grid.addWidget(self._cube_selection_combo, 1, 0)

        self.setLayout(grid)

    def bind_events(self):
        self._cube_selection_model.subscribe_update_function(self.update_cube_list_from_model)

    def update_cube_list_from_model(self):
        if self._cubes_in_file != self._cube_selection_model.cubes:
            self._cubes_in_file = self._cube_selection_model.cubes
            self._cube_selection_combo.clear()
            cube_names = get_names_from_cubes(self._cubes_in_file)
            self._cube_selection_combo.addItems(cube_names)


_select_cube_widget = SelectCubeWidget(
    get_cube_selection_model())


def get_select_cube_widget():
    return _select_cube_widget