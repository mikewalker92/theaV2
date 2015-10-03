class CubeLoadingService(object):
    def __init__(self, iris_wrapper):
        self._iris_wrapper = iris_wrapper

    def load_cubes(self, filename, cube_selection_model):
        cubes = self._iris_wrapper.load_cubes(filename)
        cube_selection_model.cubes = cubes