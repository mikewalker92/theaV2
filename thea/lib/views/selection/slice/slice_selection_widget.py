from PyQt5.QtWidgets import QGridLayout
from thea.lib.views.selection.slice.axes_widget import get_major_axes_widget
from thea.lib.views.selection.slice.collapsed_dimensions_widget import get_collapsed_dimensions_widget
from thea.lib.views.selection.slice.select_cube_widget import get_select_cube_widget
from thea.lib.views.thea_widget import TheaWidget


class SliceSelectionWidget(TheaWidget):
    def __init__(self, select_cube_widget, axes_widget, collapsed_dimensions_widget):
        super(SliceSelectionWidget, self).__init__()

        self._select_cube_widget = select_cube_widget
        self._axes_widget = axes_widget
        self._collapsed_dimensions_widget = collapsed_dimensions_widget

        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()

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
