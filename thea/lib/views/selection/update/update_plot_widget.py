from PySide import QtGui
from thea.lib.controllers.update_plot_controller import get_update_plot_controller
from thea.lib.views.thea_widget import TheaWidget


class UpdatePlotWidget(TheaWidget):
    """
    A widget for selecting the cube to figure and changing the settings for the figure.
    """

    def __init__(self, plot_controller):
        """
        :type plot_controller: thea.lib.controllers.update_plot_controller.UpdatePlotController
        """
        super(UpdatePlotWidget, self).__init__()

        self._update_button = QtGui.QPushButton('Update Plot')

        self.plot_controller = plot_controller

        self.init_ui()
        self.bind_events()

    def init_ui(self):
        self.setMaximumHeight(100)
        grid = QtGui.QGridLayout()
        grid.addWidget(self._update_button, 0, 0)
        self.setLayout(grid)

    def bind_events(self):
        self._update_button.clicked.connect(self.plot_controller.update_plot)


_update_plot_widget = UpdatePlotWidget(
    get_update_plot_controller())


def get_update_plot_widget():
    """
    :rtype: UpdatePlotWidget
    """
    return _update_plot_widget