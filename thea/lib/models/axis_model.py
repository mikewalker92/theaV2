from thea.lib.models.base_model import BaseModel


class AxisModel(BaseModel):
    """
    :type _name: str
    :type _index: int
    :type _collapse_mode: CollapseMode
    :type _collapse value: int
    """

    def __init__(self, name = None):
        super(BaseModel, self).__init__()

        self._name = name
        self._index = 0
        self._collapse_mode = None
        self._collapse_value = 0

    @property
    def name(self):
        """
        :rtype: str
        """
        return self._name