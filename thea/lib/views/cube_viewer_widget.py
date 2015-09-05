from PySide import QtGui
from thea.lib.views.cube_data_widget import CubeDataWidget
from thea.lib.views.cube_information_widget import CubeInformationWidget
from thea.lib.views.thea_widgets import TheaWidget


class CubeViewerWidget(TheaWidget):
    """
    Creates and populates a tab widget for displaying information about a cube.
    """
    def __init__(self):
        super(CubeViewerWidget, self).__init__()

        self.init_ui()

    def init_ui(self):
        tab_widget = QtGui.QTabWidget()
        tab_widget.addTab(CubeInformationWidget(), 'Cube Information')
        tab_widget.addTab(CubeInformationWidget(), 'Slice Information')
        tab_widget.addTab(CubeDataWidget(), 'Slice Data')

        layout = QtGui.QHBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)

        self.show()