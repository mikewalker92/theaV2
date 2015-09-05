from PySide import QtGui
from thea.lib.views.thea_widgets import TheaWidget


class SelectCubeWidget(TheaWidget):
    """
    A widget for selecting the cube to plot and changing the settings for the plot.
    """
    def __init__(self):
        super(SelectCubeWidget, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setMaximumHeight(80)

        grid = QtGui.QGridLayout()

        grid.addWidget(QtGui.QLabel('Current Cube'), 0, 0)
        grid.addWidget(QtGui.QComboBox(), 1, 0)

        self.setLayout(grid)

        self.show()