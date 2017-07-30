from thea.lib.models.cube_details_model import CubeDetailsModel
from thea.lib.models.user_selection_model import UserSelectionModel
from thea.lib.models.plot_model import PlotModel


class ViewModel(object):

    def __init__(self):
        self.__plot = PlotModel()
        self.__cube_details = CubeDetailsModel()
        self.__user_selection = UserSelectionModel()

    @property
    def plot(self):
        return self.__plot

    @property
    def cube_details(self):
        return self.__cube_details

    @property
    def user_selection(self):
        return self.__user_selection


__view_model = ViewModel()


def get_view_model():
    return __view_model
