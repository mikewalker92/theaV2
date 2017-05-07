from PySide import QtGui
from PySide.QtGui import QTabWidget

from thea.lib.views.selection.slice.slice_selection_widget import get_slice_selection_widget, SliceSelectionWidget
from thea.lib.views.selection.plot.plot_options_widget import get_plot_options_widget, PlotOptionsWidget
from thea.lib.views.thea_widget import TheaWidget
from thea.lib.views.selection.update.update_plot_widget import get_update_plot_widget, UpdatePlotWidget


class UserSelectionWidget(TheaWidget):
    """
    A widget for selecting the cube to figure and changing the settings for the figure.
    """
    def __init__(self, slice_selection_widget, plot_selection_widget, update_plot_widget):
        """
        :type slice_selection_widget: SliceSelectionWidget
        :type plot_selection_widget: PlotOptionsWidget
        :type update_plot_widget: UpdatePlotWidget
        """
        super(UserSelectionWidget, self).__init__()

        self._slice_selection_widget = slice_selection_widget
        self._plot_selection_widget = plot_selection_widget
        self._update_plot_widget = update_plot_widget

        self.init_ui()

    def init_ui(self):
        self.setMaximumWidth(340)

        grid = QtGui.QGridLayout()

        tab_widget = QTabWidget()
        tab_widget.addTab(self._slice_selection_widget, 'Select Sub-Cube')
        tab_widget.addTab(self._plot_selection_widget, 'Select Plot Options')

        grid.addWidget(tab_widget, 0, 0)
        grid.addWidget(self._update_plot_widget, 1, 0)

        self.setLayout(grid)


def create_user_selection_widget():
    """
    :rtype: UserSelectionWidget
    """
    return UserSelectionWidget(
        slice_selection_widget=get_slice_selection_widget(),
        plot_selection_widget=get_plot_options_widget(),
        update_plot_widget=get_update_plot_widget()
    )