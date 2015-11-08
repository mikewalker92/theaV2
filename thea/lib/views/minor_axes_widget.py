from PySide import QtGui, QtCore
from thea.lib.views.minor_axis_widget import MinorAxisWidget
from thea.lib.views.thea_widget import TheaWidget


class MinorAxesWidget(TheaWidget):
    """
    A widget for selecting the cube to plot and changing the settings for the plot.
    """
    def __init__(self, renderer):
        super(MinorAxesWidget, self).__init__(renderer)

        self._renderer = renderer

        self.init_ui()

    def init_ui(self):
        grid = QtGui.QGridLayout()
        grid.setAlignment(QtCore.Qt.AlignTop)

        grid.addWidget(QtGui.QLabel('Minor Axes'), 0, 0)
        grid.addWidget(MinorAxisWidget(self._renderer), 1, 0)
        grid.addWidget(MinorAxisWidget(self._renderer), 2, 0)

        self.setLayout(grid)

        self.show_view()