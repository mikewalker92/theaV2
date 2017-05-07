from PySide import QtGui
from thea.lib.models.view_model import get_view_model

from thea.lib.views.details.data.cube_data_widget import get_cube_data_widget
from thea.lib.views.details.cube_readout_widget import CubeReadoutWidget
from thea.lib.views.thea_widget import TheaWidget


class CubeDetailsWidget(TheaWidget):
    """
    Creates and populates a tab widget for displaying information about a cube.
    """
    def __init__(self, cube_readout_widget, slice_readout_widget, cube_data_widget):
        """
        :type cube_readout_widget: CubeReadoutWidget
        :type slice_readout_widget: CubeReadoutWidget
        :type cube_data_widget:  thea.lib.views.cube_data_widget.CubeDataWidget
        """
        super(CubeDetailsWidget, self).__init__()

        self._cube_readout_widget = cube_readout_widget
        self._slice_readout_widget = slice_readout_widget
        self._cube_data_widget = cube_data_widget

        self.init_ui()

    def init_ui(self):
        tab_widget = QtGui.QTabWidget()
        tab_widget.addTab(self._cube_readout_widget, 'Cube Readout')
        tab_widget.addTab(self._slice_readout_widget, 'Slice Readout')
        tab_widget.addTab(self._cube_data_widget, 'Slice Data')

        layout = QtGui.QHBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)


def get_cube_details_widget():
    """
    :rtype: CubeDetailsWidget
    """
    return CubeDetailsWidget(
        cube_readout_widget=CubeReadoutWidget(get_view_model().cube_details.cube_readout),
        slice_readout_widget=CubeReadoutWidget(get_view_model().cube_details.slice_readout),
        cube_data_widget=get_cube_data_widget()
    )