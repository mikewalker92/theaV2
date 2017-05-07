from PySide import QtGui
from thea.bound.target import BoundFigureCanvas
from thea.lib.models.view_model import get_view_model
from thea.lib.views.thea_widget import TheaWidget


class MatplotlibWidget(TheaWidget):
    """
    A widget for displaying matplotlib plots.
    """

    def __init__(self, plot_model):
        """
        :type plot_model: thea.lib.models.view_model.PlotModel
        """
        super(MatplotlibWidget, self).__init__()

        self._plot_model = plot_model

        # create a canvas to draw the figure on.
        self._canvas = BoundFigureCanvas(self._plot_model.figure)

        self.__init_ui()

    def __init_ui(self):
        vbl = QtGui.QVBoxLayout()
        vbl.addWidget(self._canvas)
        self.setLayout(vbl)


def get_matplotlib_widget():
    """
    :rtype: MatplotlibWidget
    """
    return MatplotlibWidget(
        plot_model=get_view_model().plot
    )