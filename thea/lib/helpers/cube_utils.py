def get_cube_names(cubes):
    """
    :type cubes: list[iris.cube.Cube]
    :rtype: list[str]
    """
    return [cube.name() for cube in cubes]