from PySide import QtGui
from PySide.QtGui import QComboBox, QLabel
from thea.lib.models.view_model import get_view_model
from thea.lib.views.thea_widget import TheaWidget


class MajorAxesWidget(TheaWidget):
    def __init__(self, view_model):
        """
        :type view_model: thea.lib.models.view_model.ViewModel
        """
        super(MajorAxesWidget, self).__init__()

        self._cube_options = view_model.options.axes_model

        self._x_axis_combo = QComboBox()
        self._y_axis_combo = QComboBox()

        self.init_ui()
        self.bind_events()

    def init_ui(self):
        self.setMaximumHeight(110)

        grid = QtGui.QGridLayout()
        grid.addWidget(QLabel('Major Axes'), 0, 0)
        grid.addWidget(self._x_axis_combo, 1, 0)
        grid.addWidget(self._y_axis_combo, 2, 0)

        self.setLayout(grid)

    def bind_events(self):
        pass

    def update_x_axis_combo(self):
        self._x_axis_combo.clear()


_major_axes_widget = MajorAxesWidget(get_view_model())


def get_major_axes_widget():
    """
    :rtype: MajorAxesWidget
    """
    return _major_axes_widget