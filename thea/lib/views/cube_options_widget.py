from PySide import QtGui
from thea.lib.views.thea_widget import TheaWidget


class CubeOptionsWidget(TheaWidget):
    """
    A widget for selecting the cube to plot and changing the settings for the plot.
    """
    def __init__(self, renderer, select_cube_widget, major_axes_widget, minor_axes_widget):
        super(CubeOptionsWidget, self).__init__(renderer)

        self._cubes_in_file = []
        self._cube_selection_combo = QtGui.QComboBox()

        self._select_cube_widget = select_cube_widget
        self._major_axes_widget = major_axes_widget
        self._minor_axes_widget = minor_axes_widget

        self.init_ui()

    def init_ui(self):
        grid = QtGui.QGridLayout()

        grid.addWidget(self._select_cube_widget, 0, 0)
        grid.addWidget(self._major_axes_widget, 1, 0)
        grid.addWidget(self._minor_axes_widget, 2, 0)

        self.setLayout(grid)

        self.show_view()
