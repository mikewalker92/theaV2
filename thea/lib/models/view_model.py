from thea.lib.models.cube_details_model import CubeDetailsModel
from thea.lib.models.user_selection_model import UserSelectionModel
from thea.lib.models.plot_model import PlotModel


class ViewModel():
    """
    :type __plot: PlotModel
    :type __cube_details: CubeDetailsModel
    :type __user_selection: UserSelectionModel
    """

    def __init__(self):
        self.__plot = PlotModel()
        self.__cube_details = CubeDetailsModel()
        self.__user_selection = UserSelectionModel()

    @property
    def plot(self):
        """
        :rtype: PlotModel
        """
        return self.__plot

    @property
    def cube_details(self):
        """
        :rtype: CubeDetailsModel
        """
        return self.__cube_details

    @property
    def user_selection(self):
        """
        :rtype: UserSelectionModel
        """
        return self.__user_selection


__view_model = ViewModel()


def get_view_model():
    """
    :rtype: ViewModel
    """
    return __view_model
