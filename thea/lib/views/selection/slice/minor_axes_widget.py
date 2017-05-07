from PySide import QtGui, QtCore
from thea.lib.views.thea_widget import TheaWidget


class CollapsedDimensionsWidget(TheaWidget):
    """
    A widget for selecting the cube to figure and changing the settings for the figure.
    """
    def __init__(self):
        super(CollapsedDimensionsWidget, self).__init__()

        self.init_ui()

    def init_ui(self):
        grid = QtGui.QGridLayout()
        grid.setAlignment(QtCore.Qt.AlignTop)

        grid.addWidget(QtGui.QLabel('Minor Axes'), 0, 0)

        self.setLayout(grid)


__minor_axes_widget = CollapsedDimensionsWidget()


def get_minor_axes_widget():
    """
    :rtype: CollapsedDimensionsWidget
    """
    return __minor_axes_widget