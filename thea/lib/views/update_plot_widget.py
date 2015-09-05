from PySide import QtGui
from thea.lib.views.thea_widgets import TheaWidget


class UpdatePlotWidget(TheaWidget):
    """
    A widget for selecting the cube to plot and changing the settings for the plot.
    """
    def __init__(self):
        super(UpdatePlotWidget, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setMaximumHeight(100)

        grid = QtGui.QGridLayout()

        grid.addWidget(QtGui.QPushButton('Update Plot'), 0, 0)

        self.setLayout(grid)

        self.show()