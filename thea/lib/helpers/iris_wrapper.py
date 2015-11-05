import iris


class IrisWrapper(object):

    @staticmethod
    def load_cubes(filename):
        return iris.load_cubes(filename)

    @staticmethod
    def cube_name(cube):
        return cube.standard_name