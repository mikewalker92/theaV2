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
    def __init__(self):
        super(OptionsWidget, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setMaximumWidth(340)

        grid = QtGui.QGridLayout()

        grid.addWidget(SelectCubeWidget(), 0, 0)
        grid.addWidget(MajorAxesWidget(), 1, 0)
        grid.addWidget(MinorAxesWidget(), 2, 0)
        grid.addWidget(UpdatePlotWidget(), 3, 0)

        self.setLayout(grid)

        self.show()