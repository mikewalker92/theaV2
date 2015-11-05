class CubeModel(object):
    def __init__(self, name='', x_axis=None, y_axis=None, minor_axes=None):
        self._name = name
        self._x_axis = x_axis
        self._y_axis = y_axis
        self._minor_axes = minor_axes

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def x_axis(self):
        return self._x_axis

    @x_axis.setter
    def x_axis(self, x_axis):
        self._x_axis = x_axis

    @property
    def y_axis(self):
        return self._y_axis

    @y_axis.setter
    def y_axis(self, y_axis):
        self._y_axis = y_axis

    @property
    def minor_axes(self):
        return self._minor_axes

    @minor_axes.setter
    def minor_axes(self, minor_axes):
        self._minor_axes = minor_axes