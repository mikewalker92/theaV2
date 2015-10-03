from PySide import QtGui
from thea.lib.views.thea_widgets import TheaWidget


class SelectCubeWidget(TheaWidget):
    """
    A widget for selecting the cube to plot and changing the settings for the plot.
    """
    def __init__(self, cube_selection_model, cube_utils):
        super(SelectCubeWidget, self).__init__()

        self._cubes_in_file = []
        self._cube_selection_combo = QtGui.QComboBox()

        self._cube_selection_model = cube_selection_model
        self._cube_utils = cube_utils

        self.init_ui()
        self.bind_events()

    def init_ui(self):
        self.setMaximumHeight(80)

        grid = QtGui.QGridLayout()

        grid.addWidget(QtGui.QLabel('Current Cube'), 0, 0)
        grid.addWidget(self._cube_selection_combo, 1, 0)

        self.setLayout(grid)

        self.show()

    def bind_events(self):
        self._cube_selection_model.subscribe_update_function(self.update_cube_list_from_model)

    def update_cube_list_from_model(self):
        if self._cubes_in_file != self._cube_selection_model.cubes:
            self._cubes_in_file = self._cube_selection_model.cubes
            self._cube_selection_combo.clear()
            cube_names = self._cube_utils.get_names_from_cubes(self._cubes_in_file)
            self._cube_selection_combo.addItems(cube_names)