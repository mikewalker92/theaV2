from PyQt5.QtWidgets import QGridLayout, QLabel
from thea.bound.target import BoundComboBox
from thea.lib.helpers.view_helper_functions import get_cube_name
from thea.lib.models.view_model import get_view_model
from thea.lib.views.thea_widget import TheaWidget


class SelectCubeWidget(TheaWidget):
    def __init__(self, cube_selection_model):
        super(SelectCubeWidget, self).__init__()

        self._cube_selection_combo = BoundComboBox(cube_selection_model.cubes, get_cube_name)

        self.init_ui()

    def init_ui(self):
        self.setMaximumHeight(88)

        grid = QGridLayout()

        grid.addWidget(QLabel('Current Cube'), 0, 0)
        grid.addWidget(self._cube_selection_combo, 1, 0)

        self.setLayout(grid)


__select_cube_widget = SelectCubeWidget(
    cube_selection_model=get_view_model().user_selection.cube_selection
)


def get_select_cube_widget():
    return __select_cube_widget
