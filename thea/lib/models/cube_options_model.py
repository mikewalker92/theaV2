from thea.lib.models.base_model import BaseModel


class CubeOptionsModel(object, BaseModel):

    _x_axis_index = 0
    _y_axis_index = 1

    def __init__(self):
        super(CubeOptionsModel, self).__init__()

    def set_x_axis_index(self, x_axis_index):
        self._x_axis_index = x_axis_index
        self.announce_update()

    def get_x_axis_index(self):
        return self._x_axis_index

    def set_y_axis_index(self, y_axis_index):
        self._y_axis_index = y_axis_index
        self.announce_update()

    def get_y_axis_index(self):
        return self._y_axis_index