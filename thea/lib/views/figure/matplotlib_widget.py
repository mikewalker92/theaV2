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

        self.__figure = None
        self.__canvas = None

        self.__plot_model = plot_model

        self.__init_ui()

    def __init_ui(self):

        # create a canvas to draw the figure on.
        self.__canvas = BoundFigureCanvas(self.__plot_model.figure)

        vbl = QtGui.QVBoxLayout()
        vbl.addWidget(self.__canvas)
        self.setLayout(vbl)


def get_matplotlib_widget():
    """
    :rtype: MatplotlibWidget
    """
    return MatplotlibWidget(
        plot_model=get_view_model().plot
    )