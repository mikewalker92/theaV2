from thea.lib.models.cube_selection_model import CubeSelectionModel
from thea.lib.models.plot_selection_model import PlotSelectionModel


class UserSelectionModel():
    """
    :type __cube_selection: CubeSelectionModel
    :type __plot_selection: PlotSelectionModel
    """

    def __init__(self):
        self.__cube_selection = CubeSelectionModel()
        self.__plot_selection = PlotSelectionModel()

    @property
    def cube_selection(self):
        """
        :rtype: CubeSelectionModel
        """
        return self.__cube_selection

    @property
    def plot_selection(self):
        """
        :rtype: PlotSelectionModel
        """
        return self.__plot_selection