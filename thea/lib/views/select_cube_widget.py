from PySide import QtGui
from thea.lib.helpers.cube_utils import get_cube_names
from thea.lib.helpers.model_provider import get_model_provider
from thea.lib.views.thea_widget import TheaWidget


class SelectCubeWidget(TheaWidget):
    """
    A widget for selecting the cube to plot and changing the settings for the plot.
    """
    def __init__(self, model_provider):
        super(SelectCubeWidget, self).__init__()

        self._cubes_in_file = []
        self._cube_selection_combo = QtGui.QComboBox()

        self._cube_selection_model = model_provider.options_model

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
        self._cubes_in_file = self._cube_selection_model.cubes
        self._cube_selection_combo.clear()
        cube_names = get_cube_names(self._cubes_in_file)
        self._cube_selection_combo.addItems(cube_names)


_select_cube_widget = SelectCubeWidget(
    get_model_provider())


def get_select_cube_widget():
    return _select_cube_widget