from PySide import QtGui
from thea.lib.views.thea_widgets import TheaWidget


class MajorAxesWidget(TheaWidget):
    def __init__(self):
        super(MajorAxesWidget, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setMaximumHeight(110)

        grid = QtGui.QGridLayout()

        grid.addWidget(QtGui.QLabel('Major Axes'), 0, 0)
        grid.addWidget(QtGui.QComboBox(), 1, 0)
        grid.addWidget(QtGui.QComboBox(), 2, 0)

        self.setLayout(grid)

        self.show()