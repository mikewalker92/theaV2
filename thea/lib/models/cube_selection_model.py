from thea.bound.source import BoundListSelection


class CubeSelectionModel(object):

    def __init__(self):
        self.__cubes = BoundListSelection([])
        self.__x_axis = BoundListSelection([])
        self.__y_axis = BoundListSelection([])

    @property
    def cubes(self):
        return self.__cubes

    @property
    def x_axis(self):
        return self.__x_axis

    @property
    def y_axis(self):
        return self.__y_axis


