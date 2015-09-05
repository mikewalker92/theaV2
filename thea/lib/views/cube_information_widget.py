from PySide import QtGui
from thea.lib.views.thea_widgets import TheaWidget


class CubeInformationWidget(TheaWidget):
    """
    A widget to display cube metadata.
    """
    def __init__(self):
        super(CubeInformationWidget, self).__init__()

        self.init_ui()

    def init_ui(self):

        self.show()