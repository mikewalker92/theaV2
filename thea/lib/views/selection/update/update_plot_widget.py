from PyQt5.QtWidgets import QGridLayout, QPushButton
from thea.lib.controllers.update_plot_controller import get_update_plot_controller
from thea.lib.views.thea_widget import TheaWidget


class UpdatePlotWidget(TheaWidget):
    def __init__(self, plot_controller):
        super(UpdatePlotWidget, self).__init__()

        self._update_button = QPushButton('Update Plot')

        self.plot_controller = plot_controller

        self.init_ui()
        self.bind_events()

    def init_ui(self):
        self.setMaximumHeight(100)
        grid = QGridLayout()
        grid.addWidget(self._update_button, 0, 0)
        self.setLayout(grid)

    def bind_events(self):
        self._update_button.clicked.connect(self.plot_controller.update_plot)


_update_plot_widget = UpdatePlotWidget(
    get_update_plot_controller())


def get_update_plot_widget():
    return _update_plot_widget
