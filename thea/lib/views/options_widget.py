from PySide import QtGui
from PySide.QtGui import QTabWidget
from thea.lib.views.minor_axes_widget import MinorAxesWidget
from thea.lib.views.major_axes_widget import MajorAxesWidget
from thea.lib.views.cube_options_widget import CubeOptionsWidget
from thea.lib.views.thea_widget import TheaWidget
from thea.lib.views.update_plot_widget import UpdatePlotWidget


class OptionsWidget(TheaWidget):
    """
    A widget for selecting the cube to plot and changing the settings for the plot.
    """
    def __init__(self, renderer, cube_options_widget, plot_options_widget, update_plot_widget):
        super(OptionsWidget, self).__init__(renderer)

        self._cube_options_widget = cube_options_widget
        self._plot_options_widget = plot_options_widget
        self._update_plot_widget = update_plot_widget

        self.init_ui()

    def init_ui(self):
        self.setMaximumWidth(340)

        grid = QtGui.QGridLayout()

        tab_widget = QTabWidget()
        tab_widget.addTab(self._cube_options_widget, 'Select Sub-Cube')
        tab_widget.addTab(self._plot_options_widget, 'Select Plot Options')

        grid.addWidget(tab_widget, 0, 0)
        grid.addWidget(self._update_plot_widget, 1, 0)

        self.setLayout(grid)

        self.show_view()