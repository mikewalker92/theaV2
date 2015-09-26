from PySide import QtGui
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from thea.lib.views.thea_widgets import TheaWidget


class MatplotlibWidget(TheaWidget):
    """
    A widget for displaying matplotlib plots.
    """
    figure = None
    canvas = None

    def __init__(self):
        super(MatplotlibWidget, self).__init__()

        self.init_ui()

    def init_ui(self):

        # get a reference to the current figure.
        self.figure = plt.gcf()

        # create a canvas to draw the figure on.
        self.canvas = FigureCanvas(self.figure)

        self.show()

    def display(self, figure):
        self.figure = figure
        self.canvas.draw()