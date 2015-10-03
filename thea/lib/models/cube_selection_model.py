from thea.lib.models.base_model import BaseModel


class CubeSelectionModel(BaseModel):

    def __init__(self):
        super(CubeSelectionModel, self).__init__()

        self._cubes = None
        self._cube_index = 0

    @property
    def cubes(self):
        return self._cubes

    @cubes.setter
    def cubes(self, value):
        self._cubes = value
        self.announce_update()

    @property
    def cube_index(self):
        return self.cube_index

    def selected_cube(self):
        return self._cubes[self._cube_index]