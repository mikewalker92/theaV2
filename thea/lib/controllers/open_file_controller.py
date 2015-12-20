class OpenFileController(object):
    def __init__(self):
        pass

    def open_file(self, filename):
        cubes = populate_cube_list(filename, cube_list_model)
        switch_to_cube(cube_list_model, index)



_open_file_controller = OpenFileController()


def get_open_file_controller():
    return _open_file_controller