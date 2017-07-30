from thea.bound.source import BoundValue


class CubeDetailsModel(object):
    def __init__(self):
        self.__cube_readout = BoundValue('')
        self.__slice_readout = BoundValue('')
        self.__slice_data = BoundValue([])

    @property
    def cube_readout(self):
        return self.__cube_readout

    @property
    def slice_readout(self):
        return self.__slice_readout

    @property
    def slice_data(self):
        return self.__slice_data