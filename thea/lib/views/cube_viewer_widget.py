from PySide import QtGui
from thea.lib.views.cube_data_widget import get_cube_data_widget
from thea.lib.views.cube_information_widget import get_cube_information_widget

from thea.lib.views.thea_widget import TheaWidget


class CubeViewerWidget(TheaWidget):
    """
    Creates and populates a tab widget for displaying information about a cube.
    """
    def __init__(self, full_cube_information_widget, cube_slice_information_widget, cube_data_widget):
        super(CubeViewerWidget, self).__init__()

        self._full_cube_information_widget = full_cube_information_widget
        self._cube_slice_information_widget = cube_slice_information_widget
        self._cube_data_widget = cube_data_widget

        self.init_ui()

    def init_ui(self):
        tab_widget = QtGui.QTabWidget()
        tab_widget.addTab(self._full_cube_information_widget, 'Cube Information')
        tab_widget.addTab(self._cube_slice_information_widget, 'Slice Information')
        tab_widget.addTab(self._cube_data_widget, 'Slice Data')

        layout = QtGui.QHBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)


_cube_viewer_widget = CubeViewerWidget(
    get_cube_information_widget(),
    get_cube_information_widget(),
    get_cube_data_widget())


def get_cube_viewer_widget():
    return _cube_viewer_widget