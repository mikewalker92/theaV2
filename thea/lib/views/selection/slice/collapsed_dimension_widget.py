from PySide import QtGui
from thea.lib.views.thea_widget import TheaWidget
from thea.resources.thea_colors import Colors


class CollapsedDimensionWidget(TheaWidget):
    """
    A widget for selecting the cube to figure and changing the settings for the figure.
    """
    def __init__(self):
        super(CollapsedDimensionWidget, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.set_foreground_color(Colors.foreground)
        self.set_background_color(Colors.background_subtle_variation)
        collapse_by = QtGui.QComboBox()
        collapse_by.addItems(["Mean", "Max", "Min", "Value"])

        grid = QtGui.QGridLayout()

        grid.addWidget(QtGui.QLabel('Axis Name'), 0, 0)
        grid.addWidget(QtGui.QLabel('Collapse by:'), 1, 0)
        grid.addWidget(collapse_by, 1, 1)
        grid.addWidget(QtGui.QLabel('Value:'), 1, 2)
        grid.addWidget(QtGui.QComboBox(), 1, 3)
        grid.addWidget(QtGui.QFrame(), 2, 0, 1, 4)

        self.setLayout(grid)