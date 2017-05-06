from thea.lib.models.base_model import BaseModel
from thea.lib.models.information_model import InformationModel
from thea.lib.models.options_model import OptionsModel
from thea.lib.models.plot_model import PlotModel


class ViewModel(BaseModel):
    """
    :type __cube: iris.cube.Cube
    :type __plot: PlotModel
    :type __information: InformationModel
    :type __options: OptionsModel
    """

    def __init__(self):
        super(ViewModel, self).__init__()

        self.__cube = None
        self.__plot = PlotModel()
        self.__information = InformationModel()
        self.__options = OptionsModel()

    @property
    def cube(self):
        """
        :rtype: iris.cube.Cube
        """
        return self.__cube

    @cube.setter
    def cube(self, value):
        """
        :param value: iris.cube.Cube
        """
        self.announce_update()
        self.__cube = value

    @property
    def plot(self):
        """
        :rtype: PlotModel
        """
        return self.__plot

    @property
    def information(self):
        """
        :rtype: InformationModel
        """
        return self.__information

    @property
    def options(self):
        """
        :rtype: OptionsModel
        """
        return self.__options

    def clear(self):
        self.cube = None
        self.plot.clear()
        self.information.clear()
        self.options.clear()


__view_model = ViewModel()


def get_view_model():
    """
    :rtype: ViewModel
    """
    return __view_model
