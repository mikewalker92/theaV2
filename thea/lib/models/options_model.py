from thea.lib.models.cube_options_model import CubeOptionsModel
from thea.lib.models.base_model import BaseModel
from thea.lib.models.plot_options_model import PlotOptionsModel


class OptionsModel(BaseModel):
    """
    :type _cube_options: CubeOptionsModel
    :type _plot_options: PlotOptionsModel
    """

    def __init__(self):
        super(OptionsModel, self).__init__()

        self._cube_options = CubeOptionsModel()
        self._plot_options = PlotOptionsModel()

    @property
    def cube_options(self):
        """
        :rtype: CubeOptionsModel
        """
        return self._cube_options

    @property
    def plot_options(self):
        """
        :rtype: PlotOptionsModel
        """
        return self._plot_options

    def clear(self):
        self._cube_options.clear()
        self._plot_options.clear()