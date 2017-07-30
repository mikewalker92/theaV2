from thea.lib.models.cube_selection_model import CubeSelectionModel
from thea.lib.models.plot_selection_model import PlotSelectionModel


class UserSelectionModel(object):

    def __init__(self):
        self.__cube_selection = CubeSelectionModel()
        self.__plot_selection = PlotSelectionModel()

    @property
    def cube_selection(self):
        return self.__cube_selection

    @property
    def plot_selection(self):
        return self.__plot_selection
