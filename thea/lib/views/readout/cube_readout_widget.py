from thea.lib.views.thea_widget import TheaWidget


class CubeReadoutWidget(TheaWidget):
    """
    A widget to display cube metadata.
    """
    def __init__(self):
        super(CubeReadoutWidget, self).__init__()

        self.init_ui()

    def init_ui(self):
        pass


_cube_readout_widget = CubeReadoutWidget()


def get_cube_readout_widget():
    """
    :rtype: CubeReadoutWidget
    """
    return _cube_readout_widget