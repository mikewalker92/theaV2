from PySide import QtGui
from thea.lib.views.thea_widget import TheaWidget


class CubeInformationWidget(TheaWidget):
    """
    A widget to display cube metadata.
    """
    def __init__(self, renderer):
        super(CubeInformationWidget, self).__init__(renderer)

        self.init_ui()

    def init_ui(self):

        self.show_view()