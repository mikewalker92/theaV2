import iris


def load_cubes_from_file(filename):
    """
    :type filename: str
    :rtype iris.cube.Cube
    """
    return iris.load_cubes(filename)