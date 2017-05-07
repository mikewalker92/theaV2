from thea.lib.services.cube_collapsing_service import get_selected_cube
from thea.lib.models.cube_selection_model import CubeSelectionModel
from thea.lib.models.user_selection_model import UserSelectionModel
from thea.lib.models.plot_selection_model import PlotSelectionModel

from iris.cube import Cube


def set_cubes_in_file(user_selection_model, cubes):
    """
    :type user_selection_model: UserSelectionModel
    :type cubes: list[Cube]
    :rtype: UserSelectionModel
    """
    user_selection_model.cube_selection.cubes.items = cubes

    # Select the first cube to start with.
    user_selection_model.cube_selection.cubes.selected_item = cubes[0]

    return user_selection_model


def populate_user_selection_model(user_selection_model):
    """
    :type user_selection_model: UserSelectionModel
    :rtype: UserSelectionModel
    """
    cube = get_selected_cube(user_selection_model)

    cube_selection_model = user_selection_model.cube_selection
    __populate_cube_selection_model(cube_selection_model, cube)

    plot_selection_model = user_selection_model.plot_selection
    __populate_plot_selection_model(plot_selection_model, cube)

    return user_selection_model


def __populate_cube_selection_model(cube_selection_model, cube):
    """
    :type cube_selection_model: CubeSelectionModel
    :type cube: Cube
    """
    cube_selection_model.x_axis.items = cube.dim_coords
    cube_selection_model.x_axis.selected_item = cube.dim_coords[0]

    cube_selection_model.y_axis.items = cube.dim_coords
    cube_selection_model.y_axis.selected_item = cube.dim_coords[1]


def __populate_plot_selection_model(plot_selection_model, cube):
    """
    :type plot_selection_model: PlotSelectionModel
    :type cube: Cube
    """
    # TODO implement this.
    pass