from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGridLayout
from thea.bound.target import BoundTextDisplay
from thea.lib.views.thea_widget import TheaWidget


class CubeReadoutWidget(TheaWidget):
    def __init__(self, cube_readout):
        super(CubeReadoutWidget, self).__init__()
        self._cube_readout_text_display = BoundTextDisplay(cube_readout)
        self.init_ui()

    def init_ui(self):
        font = QFont()
        font.setFamily('Ubuntu Mono')

        self._cube_readout_text_display.setFont(font)

        grid = QGridLayout()
        grid.addWidget(self._cube_readout_text_display)
        self.setLayout(grid)
