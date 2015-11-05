from PySide import QtGui
from PySide.QtGui import QComboBox, QLabel
from thea.lib.views.thea_widgets import TheaWidget


class MajorAxesWidget(TheaWidget):
    def __init__(self):
        super(MajorAxesWidget, self).__init__()

        self._x_axis_combo = QComboBox()
        self._y_axis_combo = QComboBox()

        self.init_ui()

    def init_ui(self):
        self.setMaximumHeight(110)

        grid = QtGui.QGridLayout()
        grid.addWidget(QLabel('Major Axes'), 0, 0)
        grid.addWidget(self._x_axis_combo, 1, 0)
        grid.addWidget(self._y_axis_combo, 2, 0)

        self.setLayout(grid)

        self.show()