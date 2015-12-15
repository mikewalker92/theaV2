from thea.lib.views.thea_widget import TheaWidget


class CubeDataWidget(TheaWidget):
    """
    A table to display data from a 2D slice through a cube.
    """
    def __init__(self):
        super(CubeDataWidget, self).__init__()

        self.init_ui()

    def init_ui(self):
        pass

_cube_data_widget = CubeDataWidget()


def get_cube_data_widget():
    return _cube_data_widget