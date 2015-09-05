from PySide import QtGui
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from thea.lib.views.thea_widgets import TheaWidget


class MatplotlibWidget(TheaWidget):
    """
    A widget for displaying matplotlib plots.
    """
    def __init__(self):
        super(MatplotlibWidget, self).__init__()

        self.init_ui()

    def init_ui(self):

        # get a reference to the current figure.
        figure = plt.gcf()

        # create a canvas to draw the figure on.
        canvas = FigureCanvas(figure)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(canvas)
        self.setLayout(vbox)

        self.show()