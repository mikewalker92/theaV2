from thea.lib.helpers.cube_utils import load_cubes
from thea.lib.services.cube_axes_service import populate_major_axes, populate_minor_axes
from thea.lib.services.cube_metadata_service import populate_metadata


def load_file(filename, cube_selection_model):
    cubes = load_cubes(filename)
    cube_selection_model.cubes = cubes
    cube_selection_model.cube_index = 0
    load_cube(cube_selection_model)


def load_cube(cube_selection_model):
    cube = cube_selection_model.selected_cube()
    populate_major_axes(cube)
    populate_minor_axes(cube)
    populate_metadata(cube)

