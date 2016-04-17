

def populate_view(options_model, information_model):
    """
    :type options_model: thea.lib.models.options_model.OptionsModel
    :type information_model: thea.lib.models.information_model.InformationModel
    """
    cube = options_model.cubes[options_model.cube_index]
    _populate_options_model(cube, options_model)
    _populate_information_model(cube, information_model)


def _populate_options_model(cube, options_model):
    """
    :type cube: iris.cube.Cube
    :type options_model: thea.lib.models.options_model.OptionsModel
    """
    pass


def _populate_information_model(cube, information_model):
    """
    :type cube: iris.cube.Cube
    :type information_model: thea.lib.models.information_model.InformationModel
    """
    pass