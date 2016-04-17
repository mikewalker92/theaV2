import iris


def load_file(filename, options_model):
    """
    :type filename: str
    :type options_model: thea.lib.models.options_model.OptionsModel
    """
    options_model.add_cubes(iris.load_cubes(filename))