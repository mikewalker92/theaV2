from PySide import QtGui
from PySide.QtGui import QTabWidget
from thea.lib.views.minor_axes_widget import MinorAxesWidget
from thea.lib.views.major_axes_widget import MajorAxesWidget
from thea.lib.views.select_cube_widget import SelectCubeWidget
from thea.lib.views.thea_widgets import TheaWidget
from thea.lib.views.update_plot_widget import UpdatePlotWidget


class OptionsWidget(TheaWidget):
    """
    A widget for selecting the cube to plot and changing the settings for the plot.
    """
    def __init__(self, select_plotted_cube_widget, plot_options_widget, update_plot_widget):
        super(OptionsWidget, self).__init__()

        self._select_plotted_cube_widget = select_plotted_cube_widget
        self._plot_options_widget = plot_options_widget
        self._update_plot_widget = update_plot_widget

        self.init_ui()

    def init_ui(self):
        self.setMaximumWidth(340)

        grid = QtGui.QGridLayout()

        tab_widget = QTabWidget()
        tab_widget.addTab(self._select_plotted_cube_widget, 'Select Sub-Cube')
        tab_widget.addTab(self._plot_options_widget, 'Select Plot Options')

        grid.addWidget(tab_widget, 0, 0)
        grid.addWidget(self._update_plot_widget, 1, 0)

        self.setLayout(grid)

        self.show()