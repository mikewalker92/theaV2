from thea.lib.helpers.axis_model_factory import create_axis_model


def populate_view(view_model):
    """
    :type view_model: thea.lib.models.view_model.ViewModel
    """
    _cube_options = view_model.options.cube_options
    _cube = _cube_options.cubes[_cube_options.cube_index]

    view_model.cube = _cube
    _populate_options_model(_cube, _cube_options)
    _populate_information_model(_cube, view_model.information)


def _populate_options_model(cube, options_model):
    """
    :type cube: iris.cube.Cube
    :type options_model: thea.lib.models.cube_options_model.CubeOptionsModel
    """
    dimensions = cube.dim_coords
    for counter, dimension in enumerate(dimensions):
        if counter == 0:
            options_model.x_axis = create_axis_model(dimension)
        elif counter == 1:
            options_model.y_axis = create_axis_model(dimension)
        else:
            options_model.add_collapsed_axis(create_axis_model(dimension))

    options_model.axis_names = [dimension.name() for dimension in dimensions]


def _populate_information_model(cube, information_model):
    """
    :type cube: iris.cube.Cube
    :type information_model: thea.lib.models.information_model.InformationModel
    """
    pass