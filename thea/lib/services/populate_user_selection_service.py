from thea.lib.services.cube_collapsing_service import get_selected_cube


def set_cubes_in_file(user_selection_model, cubes):
    """
    :type user_selection_model: thea.lib.models.user_selection_model.UserSelectionModel
    :type cubes: list[iris.cube.Cube]
    :rtype: thea.lib.models.user_selection_model.UserSelectionModel
    """
    user_selection_model.cube_selection.cubes.items = cubes

    # Select the first cube to start with.
    user_selection_model.cube_selection.cubes.selected_item = cubes[0]

    return user_selection_model


def populate_user_selection_model(user_selection_model):
    """
    :type user_selection_model: thea.lib.models.user_selection_model.UserSelectionModel
    :rtype: thea.lib.models.user_selection_model.UserSelectionModel
    """
    cube = get_selected_cube(user_selection_model)

    cube_selection_model = user_selection_model.cube_selection
    __populate_cube_selection_model(cube_selection_model, cube)

    plot_selection_model = user_selection_model.plot_selection
    __populate_plot_selection_model(plot_selection_model, cube)

    return user_selection_model


def __populate_cube_selection_model(cube_selection_model, cube):
    """
    :type cube_selection_model: thea.lib.models.cube_selection_model.CubeSelectionModel
    :type cube: iris.cube.Cube
    """
    # TODO implement this
    pass


def __populate_plot_selection_model(plot_selection_model, cube):
    """
    :type plot_selection_model: thea.lib.models.plot_selection_model.PlotSelectionModel
    :type cube: iris.cube.Cube
    """
    # TODO implement this.
    pass