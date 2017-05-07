from PySide import QtGui
from PySide.QtGui import QTabWidget

from thea.lib.views.selection.slice.cube_options_widget import get_cube_options_widget
from thea.lib.views.selection.plot.plot_options_widget import get_plot_options_widget
from thea.lib.views.thea_widget import TheaWidget
from thea.lib.views.selection.update.update_plot_widget import get_update_plot_widget


class UserSelectionWidget(TheaWidget):
    """
    A widget for selecting the cube to figure and changing the settings for the figure.
    """
    def __init__(self, cube_options_widget, plot_options_widget, update_plot_widget):
        """
        :type cube_options_widget: thea.lib.views.cube_options_widget.CubeOptionsWidget
        :type plot_options_widget: thea.lib.views.plot_options_widget.PlotOptionsWidget
        :type update_plot_widget: thea.lib.views.update_plot_widget.UpdatePlotWidget
        """
        super(UserSelectionWidget, self).__init__()

        self._cube_options_widget = cube_options_widget
        self._plot_options_widget = plot_options_widget
        self._update_plot_widget = update_plot_widget

        self.init_ui()

    def init_ui(self):
        self.setMaximumWidth(340)

        grid = QtGui.QGridLayout()

        tab_widget = QTabWidget()
        tab_widget.addTab(self._cube_options_widget, 'Select Sub-Cube')
        tab_widget.addTab(self._plot_options_widget, 'Select Plot Options')

        grid.addWidget(tab_widget, 0, 0)
        grid.addWidget(self._update_plot_widget, 1, 0)

        self.setLayout(grid)


_user_selection_widget = UserSelectionWidget(
    get_cube_options_widget(),
    get_plot_options_widget(),
    get_update_plot_widget())


def create_user_selection_widget():
    """
    :rtype: UserSelectionWidget
    """
    return _user_selection_widget