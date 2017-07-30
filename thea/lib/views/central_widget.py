from PyQt5.QtWidgets import QSplitter, QGridLayout
from PyQt5.QtCore import Qt
from thea.lib.views.details.cube_details_widget import get_cube_details_widget
from thea.lib.views.figure.matplotlib_widget import get_matplotlib_widget
from thea.lib.views.selection.user_selection_widget import create_user_selection_widget
from thea.lib.views.thea_widget import TheaWidget
from thea.resources.thea_colors import Colors


class CentralWidget(TheaWidget):
    def __init__(self, matplotlib_widget, cube_details_widget, user_selection_widget):
        super(CentralWidget, self).__init__()

        self._matplotlib_widget = matplotlib_widget
        self._cube_details_widget = cube_details_widget
        self._user_selection_widget = user_selection_widget

        self.init_ui()

    def init_ui(self):
        self.set_background_color(Colors.background_accent)

        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(self._matplotlib_widget)
        splitter.addWidget(self._cube_details_widget)

        grid = QGridLayout()
        grid.addWidget(splitter, 1, 0, 2, 1)
        grid.addWidget(self._user_selection_widget, 1, 1, 2, 1)
        self.setLayout(grid)


def create_central_widget():
    return CentralWidget(
        matplotlib_widget=get_matplotlib_widget(),
        cube_details_widget=get_cube_details_widget(),
        user_selection_widget=create_user_selection_widget()
    )
