from PyQt5.QtWidgets import QLabel, QComboBox, QFrame, QGridLayout
from thea.lib.views.thea_widget import TheaWidget
from thea.resources.thea_colors import Colors


class CollapsedDimensionWidget(TheaWidget):
    def __init__(self):
        super(CollapsedDimensionWidget, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.set_foreground_color(Colors.foreground)
        self.set_background_color(Colors.background_subtle_variation)
        collapse_by = QComboBox()
        collapse_by.addItems(["Mean", "Max", "Min", "Value"])

        grid = QGridLayout()

        grid.addWidget(QLabel('Axis Name'), 0, 0)
        grid.addWidget(QLabel('Collapse by:'), 1, 0)
        grid.addWidget(collapse_by, 1, 1)
        grid.addWidget(QLabel('Value:'), 1, 2)
        grid.addWidget(QComboBox(), 1, 3)
        grid.addWidget(QFrame(), 2, 0, 1, 4)

        self.setLayout(grid)
