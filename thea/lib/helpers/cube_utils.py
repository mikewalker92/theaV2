import iris


def load_cubes(filename):
    return iris.load_cubes(filename)


def cube_name(cube):
    return cube.standard_name


def get_names_from_cubes(cubes):
    return [cube_name(cube) for cube in cubes]


def collapse_cube(cube_selection_model):
    return cube_selection_model.selected_cube()