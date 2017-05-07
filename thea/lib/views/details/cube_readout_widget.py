from PySide import QtGui
from thea.bound.target import BoundTextDisplay
from thea.lib.models.view_model import get_view_model
from thea.lib.views.thea_widget import TheaWidget


class CubeReadoutWidget(TheaWidget):
    """
    A widget to display a readable representation of the cube's metadata.
    """
    def __init__(self, cube_readout):
        super(CubeReadoutWidget, self).__init__()
        self.__cube_readout_text_display = BoundTextDisplay(cube_readout)
        self.init_ui()

    def init_ui(self):
        grid = QtGui.QGridLayout()
        grid.addWidget(self.__cube_readout_text_display)
        self.setLayout(grid)