class CubeController(object):
    def __init__(self, cube_loading_service):
        self.cube_loading_service = cube_loading_service

    def load_cubes(self, filename):
        self.cube_loading_service.load_cubes(filename)
