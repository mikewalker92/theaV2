from PySide.QtGui import QGridLayout
from thea.lib.views.thea_widgets import TheaWidget


class SelectPlottedCubeWidget(TheaWidget):

    _cube_model = None

    def __init__(self, select_cube_widget, major_axes_widget, minor_axes_widget):
        super(SelectPlottedCubeWidget, self).__init__()

        self._select_cube_widget = select_cube_widget
        self._major_axes_widget = major_axes_widget
        self._minor_axes_widget = minor_axes_widget

        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()

        grid.addWidget(self._select_cube_widget, 0, 0)
        grid.addWidget(self._major_axes_widget, 1, 0)
        grid.addWidget(self._minor_axes_widget, 2, 0)

        self.setLayout(grid)

        self.show()

    def set_cube_model(self, cube_model):
        self._cube_model = cube_model
        self._major_axes_widget.set_x_axis(cube_model.x_axis)
        self._major_axes_widget.set_y_axis(cube_model.y_axis)
        self._minor_axes_widget.set_minor_axes(cube_model.minor_axis)
