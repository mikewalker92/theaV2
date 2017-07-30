from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import QComboBox, QPlainTextEdit, QTableView
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from numpy import asscalar


class BoundComboBox(QComboBox):

    def __init__(self, bound_list_selection, to_label_function):
        super(BoundComboBox, self).__init__()

        bound_list_selection.subscribe(self)
        self.__to_label_function = to_label_function

        self.update_bound_target(bound_list_selection)

    def update_bound_target(self, bound_list_selection):
        self.clear()

        labels = [self.__to_label_function(item) for item in bound_list_selection.items]
        self.addItems(labels)

        self.setCurrentIndex(bound_list_selection.current_index)


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


class BoundTableView(QTableView):

    def __init__(self, bound_array):
        self.__table_model = BoundTableModel(bound_array)
        super(BoundTableView, self).__init__()
        bound_array.subscribe(self)

    def update_bound_target(self, bound_array):
        self.clearSpans()
        self.__table_model.update_bound_target(bound_array)
        self.setModel(self.__table_model)


class BoundTableModel(QAbstractTableModel):

    def __init__(self, bound_array):
        self.__data_array = bound_array.value
        super(BoundTableModel, self).__init__()

    def rowCount(self, parent):
        return len(self.__data_array)

    def columnCount(self, parent):
        return len(self.__data_array[0])

    def data(self, index, role):
        if not role == Qt.DisplayRole:
            return None

        if not index.isValid():
            return None

        value = self.__data_array[index.row()][index.column()]

        # The cube contains numpy numeric types instead of native python types, so we use
        # 'asscalar()' here to convert them back.
        return asscalar(value)

    def update_bound_target(self, bound_array):
        self.__data_array = bound_array.value
