from thea.lib.services.cube_collapsing_service import get_selected_cube


def set_cubes_in_file(user_selection_model, cubes):
    user_selection_model.cube_selection.cubes.items = cubes

    # Select the first cube to start with.
    user_selection_model.cube_selection.cubes.selected_item = cubes[0]

    return user_selection_model


def populate_user_selection_model(user_selection_model):
    cube = get_selected_cube(user_selection_model)

    cube_selection_model = user_selection_model.cube_selection
    __populate_cube_selection_model(cube_selection_model, cube)

    plot_selection_model = user_selection_model.plot_selection
    __populate_plot_selection_model(plot_selection_model, cube)

    return user_selection_model


def __populate_cube_selection_model(cube_selection_model, cube):
    cube_selection_model.x_axis.items = cube.dim_coords
    cube_selection_model.x_axis.selected_item = cube.dim_coords[0]

    cube_selection_model.y_axis.items = cube.dim_coords
    cube_selection_model.y_axis.selected_item = cube.dim_coords[1]


def __populate_plot_selection_model(plot_selection_model, cube):
    # TODO implement this.
    pass
