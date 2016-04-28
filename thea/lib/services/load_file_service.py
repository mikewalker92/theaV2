import iris


def load_file(filename, cube_options_model):
    """
    :type filename: str
    :type cube_options_model: thea.lib.models.cube_options_model.CubeOptionsModel
    """
    cube_options_model.add_cubes(iris.load_cubes(filename))