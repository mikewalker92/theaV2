class AxisModel(object):
    def __init__(self, name='', index=0):
        self._name = name
        self._index = index

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, index):
        self._index = index

_axis_model = AxisModel()


def get_axis_model():
    return _axis_model