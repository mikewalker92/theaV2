import iris


class IrisWrapper(object):

    @staticmethod
    def load_cubes(filename):
        return iris.load_cubes(filename)