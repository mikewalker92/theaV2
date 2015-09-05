from PySide import QtGui
from thea.lib.views.thea_widgets import TheaWidget


class CubeDataWidget(TheaWidget):
    """
    A table to display data from a 2D slice through a cube.
    """
    def __init__(self):
        super(CubeDataWidget, self).__init__()

        self.init_ui()

    def init_ui(self):

        self.show()