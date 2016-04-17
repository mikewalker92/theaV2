def get_cube_names(cubes):
    """
    :type cubes: list[iris.cube.Cube]
    :rtype: list[str]
    """
    return [get_name(cube) for cube in cubes]


def get_name(cube):
    """
    :type cube: iris.cube.Cube
    :rtype: str
    """
    if cube.long_name is not None:
        return cube.long_name
    if cube.standard_name is not None:
        return cube.standard_name
    if cube.var_name is not None:
        return cube.var_name
    return "Unknown"