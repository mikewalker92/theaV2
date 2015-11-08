from PySide import QtGui
from thea.lib.helpers.renderer import Renderer
from thea.resources.thea_colors import Colors


class TheaWidget(QtGui.QWidget):
    def __init__(self, renderer):
        super(TheaWidget, self).__init__()

        self._renderer = renderer
        self.setAutoFillBackground(True)
        self.set_background_color(Colors.background)
        self.set_foreground_color(Colors.highlight)

    def set_background_color(self, color):
        palette = self.palette()
        palette.setColor(self.backgroundRole(), color)
        self.setPalette(palette)

    def set_foreground_color(self, color):
        palette = self.palette()
        palette.setColor(self.foregroundRole(), color)
        self.setPalette(palette)

    def show_view(self):
        self._renderer.show(self)