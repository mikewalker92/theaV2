from thea.lib.models.axis_model import AxisModel
from thea.lib.models.base_model import BaseModel


class CubeOptionsModel(BaseModel):
    """
    :type _cubes: list[iris.cube.Cube]
    :type _cube_index: int
    :type _x_axis: thea.lib.models.axis_model.AxisModel
    :type _y_axis: thea.lib.models.axis_model.AxisModel
    :type _collapsed_dims: list[thea.lib.models.axis_model.AxisModel]
    :type _axis_names: list[str]
    """

    def __init__(self):
        super(CubeOptionsModel, self).__init__()

        self._cubes = []
        self._cube_index = 0
        self._x_axis = AxisModel()
        self._y_axis = AxisModel()
        self._collapsed_dims = []
        self._axis_names = []

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
        :type index: int
        """
        self.announce_update()
        self._cube_index = index

    @property
    def x_axis(self):
        """
        :rtype: AxisModel
        """
        return self._x_axis

    @x_axis.setter
    def x_axis(self, x_axis):
        """
        :type x_axis: AxisModel
        """
        self._x_axis = x_axis

    @property
    def y_axis(self):
        """
        :rtype: AxisModel
        """
        return self._y_axis

    @y_axis.setter
    def y_axis(self, y_axis):
        """
        :type y_axis: AxisModel
        """
        self._y_axis = y_axis

    @property
    def collapsed_axes(self):
        """
        :rtype: list[AxisModel]
        """
        return self.collapsed_axes

    def add_collapsed_axis(self, dimension):
        """
        :type dimension: AxisModel
        """
        self._collapsed_dims.append(dimension)
        self.announce_update()

    @property
    def axis_names(self):
        """
        :return: list[str]
        """
        return self._axis_names

    @axis_names.setter
    def axis_names(self, axis_names):
        """
        :param axis_names: list[str]
        """
        self._axis_names = axis_names
        self.announce_update()


