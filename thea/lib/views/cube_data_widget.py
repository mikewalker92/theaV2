from PySide import QtGui
from thea.lib.views.thea_widget import TheaWidget


class CubeDataWidget(TheaWidget):
    """
    A table to display data from a 2D slice through a cube.
    """
    def __init__(self, renderer):
        super(CubeDataWidget, self).__init__(renderer)

        self.init_ui()

    def init_ui(self):

        self.show_view()