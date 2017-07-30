from PyQt5.QtWidgets import QHBoxLayout
from thea.bound.target import BoundTableView
from thea.lib.models.view_model import get_view_model
from thea.lib.views.thea_widget import TheaWidget


class SliceDataWidget(TheaWidget):
    """
    A table to display data from a 2D slice through a cube.
    """
    def __init__(self, slice_data):
        super(SliceDataWidget, self).__init__()

        self._cube_data_table = BoundTableView(slice_data)

        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()
        layout.addWidget(self._cube_data_table)
        self.setLayout(layout)


def create_slice_data_widget():
    """
    :rtype: SliceDataWidget
    """
    return SliceDataWidget(
        slice_data=get_view_model().cube_details.slice_data
    )