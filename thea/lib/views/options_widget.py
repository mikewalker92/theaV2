from PySide import QtGui
from thea.lib.views.minor_axes_widget import MinorAxesWidget
from thea.lib.views.major_axes_widget import MajorAxesWidget
from thea.lib.views.select_cube_widget import SelectCubeWidget
from thea.lib.views.thea_widgets import TheaWidget
from thea.lib.views.update_plot_widget import UpdatePlotWidget


class OptionsWidget(TheaWidget):
    """
    A widget for selecting the cube to plot and changing the settings for the plot.
    """
    def __init__(self, select_cube_widget, major_axes_widget, minor_axes_widget, update_plot_widget):
        super(OptionsWidget, self).__init__()

        self._select_cube_widget = select_cube_widget
        self._major_axes_widget = major_axes_widget
        self._minor_axes_widget = minor_axes_widget
        self._update_plot_widget = update_plot_widget

        self.init_ui()

    def init_ui(self):
        self.setMaximumWidth(340)

        grid = QtGui.QGridLayout()

        grid.addWidget(self._select_cube_widget, 0, 0)
        grid.addWidget(self._major_axes_widget, 1, 0)
        grid.addWidget(self._minor_axes_widget, 2, 0)
        grid.addWidget(self._update_plot_widget, 3, 0)

        self.setLayout(grid)

        self.show()