from PySide.QtGui import QComboBox, QPlainTextEdit
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

from thea.bound.source import BoundListSelection


class BoundComboBox(QComboBox):

    def __init__(self, bound_list_selection, to_label_function):
        """
        :type bound_list_selection: BoundListSelection
        :type to_label_function: function
        """
        super(BoundComboBox, self).__init__()

        bound_list_selection.subscribe(self)
        self.__to_label_function = to_label_function

        self.update_bound_target(bound_list_selection)

    def update_bound_target(self, bound_list_selection):
        """
        :type bound_list_selection: BoundListSelection
        """
        self.clear()

        labels = [self.__to_label_function(item) for item in bound_list_selection.items]
        self.addItems(labels)


class BoundFigureCanvas(FigureCanvas):

    def __init__(self, bound_figure):
        super(BoundFigureCanvas, self).__init__(bound_figure.value)

        bound_figure.subscribe(self)

    def update_bound_target(self, bound_figure):
        self.figure = bound_figure.value
        self.draw()


class BoundTextDisplay(QPlainTextEdit):

    def __init__(self, bound_text):
        super(BoundTextDisplay, self).__init__()

        bound_text.subscribe(self)

        self.update_bound_target(bound_text)
        self.setReadOnly(True)

    def update_bound_target(self, bound_text):
        self.setPlainText(bound_text.value)
