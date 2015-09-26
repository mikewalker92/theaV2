from thea.lib.models.base_model import BaseModel


class CubeSelectionModel(BaseModel):

    def __init__(self):
        super(CubeSelectionModel, self).__init__()

        self._cube = None

    def set_cube(self, cube):
        self._cube = cube
        self.announce_update()

    def get_cube(self):
        return self._cube