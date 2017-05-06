from PySide.QtGui import QComboBox
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas


class BoundComboBox(QComboBox):

    def __init__(self, bound_list_selection, to_label_function, *args, **kwargs):
        super(BoundComboBox, self).__init__(*args, **kwargs)

        bound_list_selection.subscribe(self)
        self.__to_label_function = to_label_function

    def update_bound_target(self, bound_combo_selection):
        self.clear()

        labels = [self.__to_label_function(item) for item in bound_combo_selection]
        self.addItems(labels)


class BoundFigureCanvas(FigureCanvas):

    def __init__(self, bound_figure):
        self.__figure = bound_figure.value

        super(BoundFigureCanvas, self).__init__(self.__figure)

        bound_figure.subscribe(self)

    def update_bound_target(self, bound_figure):
        self.__figure = bound_figure
        self.draw()