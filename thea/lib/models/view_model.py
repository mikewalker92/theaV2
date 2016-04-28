from thea.lib.models.base_model import BaseModel
from thea.lib.models.information_model import InformationModel
from thea.lib.models.options_model import OptionsModel
from thea.lib.models.plot_model import PlotModel


class ViewModel(BaseModel):
    """
    :type _cube: iris.cube.Cube
    :type _plot: PlotModel
    :type _information: InformationModel
    :type _options: OptionsModel
    """

    def __init__(self):
        super(ViewModel, self).__init__()

        self._cube = None
        self._plot = PlotModel()
        self._information = InformationModel()
        self._options = OptionsModel()

    @property
    def cube(self):
        """
        :rtype: iris.cube.Cube
        """
        return self._cube

    @cube.setter
    def cube(self, value):
        """
        :param value: iris.cube.Cube
        """
        self.announce_update()
        self._cube = value

    @property
    def plot(self):
        """
        :rtype: PlotModel
        """
        return self._plot

    @property
    def information(self):
        """
        :rtype: InformationModel
        """
        return self._information

    @property
    def options(self):
        """
        :rtype: OptionsModel
        """
        return self._options

    def clear(self):
        self.cube = None
        self.plot.clear()
        self.information.clear()
        self.options.clear()


_view_model = ViewModel()


def get_view_model():
    """
    :rtype: ViewModel
    """
    return _view_model
