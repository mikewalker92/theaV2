from PyQt5.QtWidgets import QTabWidget, QHBoxLayout
from thea.lib.models.view_model import get_view_model
from thea.lib.views.details.data.cube_data_widget import create_slice_data_widget
from thea.lib.views.details.cube_readout_widget import CubeReadoutWidget
from thea.lib.views.thea_widget import TheaWidget


class CubeDetailsWidget(TheaWidget):
    def __init__(self, cube_readout_widget, slice_readout_widget, slice_data_widget):
        super(CubeDetailsWidget, self).__init__()

        self._cube_readout_widget = cube_readout_widget
        self._slice_readout_widget = slice_readout_widget
        self._slice_data_widget = slice_data_widget

        self.init_ui()

    def init_ui(self):
        tab_widget = QTabWidget()
        tab_widget.addTab(self._cube_readout_widget, 'Cube Readout')
        tab_widget.addTab(self._slice_readout_widget, 'Slice Readout')
        tab_widget.addTab(self._slice_data_widget, 'Slice Data')

        layout = QHBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)


def get_cube_details_widget():
    return CubeDetailsWidget(
        cube_readout_widget=CubeReadoutWidget(get_view_model().cube_details.cube_readout),
        slice_readout_widget=CubeReadoutWidget(get_view_model().cube_details.slice_readout),
        slice_data_widget=create_slice_data_widget()
    )
