from PyQt5.QtWidgets import QGridLayout, QLabel
from thea.lib.views.thea_widget import TheaWidget


class CollapsedDimensionsWidget(TheaWidget):
    def __init__(self):
        super(CollapsedDimensionsWidget, self).__init__()
        self._collapsed_dimensions = []
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()

        grid.addWidget(QLabel('Minor Axes'), 0, 0)

        self.setLayout(grid)


def get_collapsed_dimensions_widget():
    return CollapsedDimensionsWidget()