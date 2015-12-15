from thea.lib.models.base_model import BaseModel


class CubeSelectionModel(BaseModel):

    def __init__(self):
        super(CubeSelectionModel, self).__init__()

        self._cubes = []
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
        return self._cube_index

    @cube_index.setter
    def cube_index(self, index):
        self._cube_index = index

    def selected_cube(self):
        return self._cubes[self._cube_index]


_cube_selection_model = CubeSelectionModel()


def get_cube_selection_model():
    return _cube_selection_model