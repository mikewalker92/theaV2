from thea.lib.views.thea_widget import TheaWidget


class CubeInformationWidget(TheaWidget):
    """
    A widget to display cube metadata.
    """
    def __init__(self):
        super(CubeInformationWidget, self).__init__()

        self.init_ui()

    def init_ui(self):
        pass


_cube_information_widget = CubeInformationWidget()


def get_cube_information_widget():
    """
    :rtype: CubeInformationWidget
    """
    return _cube_information_widget