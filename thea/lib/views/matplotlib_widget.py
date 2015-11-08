from PySide import QtGui
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from thea.lib.views.thea_widget import TheaWidget


class MatplotlibWidget(TheaWidget):
    """
    A widget for displaying matplotlib plots.
    """

    def __init__(self, renderer, plot_model):
        super(MatplotlibWidget, self).__init__(renderer)

        self._figure = None
        self._canvas = None
        self._plot_model = plot_model

        self.init_ui()
        self.bind_events()

    def init_ui(self):

        # get a reference to the current figure.
        self._figure = plt.gcf()

        # create a canvas to draw the figure on.
        self._canvas = FigureCanvas(self._figure)

        vbl = QtGui.QVBoxLayout()
        vbl.addWidget(self._canvas)
        self.setLayout(vbl)

        self.show_view()

    def bind_events(self):
        self._plot_model.subscribe_update_function(self.update_figure_from_model)

    def update_figure_from_model(self):
        if self._figure != self._plot_model.current_plot:
            self._figure = self._plot_model.current_plot
            self._canvas.draw()