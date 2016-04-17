from thea.lib.models.axes_model import AxesModel
from thea.lib.models.base_model import BaseModel
from thea.lib.models.plot_options_model import PlotOptions


class OptionsModel(BaseModel):
    """
    :type _cubes: list[iris.cube.Cube]
    :type _cube_index: int
    :type _axes_model: AxesModel
    :type _plot_options: PlotOptions
    """

    def __init__(self):
        super(OptionsModel, self).__init__()

        self._cubes = []
        self._cube_index = 0
        self._axes_model = AxesModel()
        self._plot_options = PlotOptions()

    @property
    def cubes(self):
        """
        :rtype: list[iris.cube.Cube]
        """
        return self._cubes

    def add_cubes(self, cubes):
        """
        :type cubes: list[iris.cube.Cube]
        """
        self.announce_update()
        self._cubes.extend(cubes)

    @property
    def cube_index(self):
        """
        :rtype: int
        """
        return self._cube_index

    @cube_index.setter
    def cube_index(self, index):
        """
        :param index: int
        """
        self.announce_update()
        self._cube_index = index

    @property
    def current_cube(self):
        """
        :rtype: iris.cube.Cube
        """
        return self._cubes[self._cube_index]

    @property
    def axes_model(self):
        """
        :rtype: AxesModel
        """
        return self._axes_model

    @property
    def plot_options(self):
        """
        :rtype: PlotOptions
        """
        return self._plot_options

    def clear(self):
        self._cubes = []
        self._cube_index = 0
        self._axes_model.clear()
        self._plot_options.clear()