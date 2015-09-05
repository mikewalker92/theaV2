from PySide import QtGui, QtCore
from thea.lib.views.minor_axis_widget import MinorAxisWidget
from thea.lib.views.thea_widgets import TheaWidget


class MinorAxesWidget(TheaWidget):
    """
    A widget for selecting the cube to plot and changing the settings for the plot.
    """
    def __init__(self):
        super(MinorAxesWidget, self).__init__()

        self.init_ui()

    def init_ui(self):
        grid = QtGui.QGridLayout()
        grid.setAlignment(QtCore.Qt.AlignTop)

        grid.addWidget(QtGui.QLabel('Major Axes'), 0, 0)
        grid.addWidget(MinorAxisWidget(), 1, 0)
        grid.addWidget(MinorAxisWidget(), 2, 0)

        self.setLayout(grid)

        self.show()