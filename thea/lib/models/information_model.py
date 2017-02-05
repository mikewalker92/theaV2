from thea.lib.models.base_model import BaseModel


class InformationModel(BaseModel):
    """
    :type _printed_cube: str
    """
    def __init__(self):
        super(InformationModel, self).__init__()
        self._printed_cube = ''

    @property
    def printed_cube(self):
        return self._printed_cube

    @printed_cube.setter
    def printed_cube(self, printed_cube):
        self._printed_cube = printed_cube
        self.announce_update()