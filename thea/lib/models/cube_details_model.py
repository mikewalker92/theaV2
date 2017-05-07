from thea.bound.source import BoundValue


class CubeDetailsModel():
    """
    :type __cube_readout: thea.bound.source.BoundValue
    :type __slice_readout: thea.bound.source.BoundValue
    :type __slice_data: thea.bound.source.BoundValue
    """
    def __init__(self):
        self.__cube_readout = BoundValue('')
        self.__slice_readout = BoundValue('')
        self.__slice_data = BoundValue([])

    @property
    def cube_readout(self):
        """
        :rtype: thea.bound.source.BoundValue
        """
        return self.__cube_readout

    @property
    def slice_readout(self):
        """
        :rtype: thea.bound.source.BoundValue
        """
        return self.__slice_readout

    @property
    def slice_data(self):
        """
        :rtype: thea.bound.source.BoundValue
        """
        return self.__slice_data