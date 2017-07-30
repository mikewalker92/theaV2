from PyQt5.QtWidgets import QVBoxLayout
from thea.bound.target import BoundFigureCanvas
from thea.lib.models.view_model import get_view_model
from thea.lib.views.thea_widget import TheaWidget


class MatplotlibWidget(TheaWidget):

    def __init__(self, plot_model):
        super(MatplotlibWidget, self).__init__()

        self._plot_model = plot_model

        # create a canvas to draw the figure on.
        self._canvas = BoundFigureCanvas(self._plot_model.figure)

        self.__init_ui()

    def __init_ui(self):
        vbl = QVBoxLayout()
        vbl.addWidget(self._canvas)
        self.setLayout(vbl)


def get_matplotlib_widget():
    return MatplotlibWidget(
        plot_model=get_view_model().plot
    )
