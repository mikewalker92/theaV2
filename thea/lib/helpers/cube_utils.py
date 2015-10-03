class CubeUtils(object):

    def __init__(self, iris_wrapper):
        self._iris = iris_wrapper

    def get_names_from_cubes(self, cubes):
        return [self.get_name_from_cube(cube) for cube in cubes]

    def get_name_from_cube(self, cube):
        return self._iris.cube_name(cube)