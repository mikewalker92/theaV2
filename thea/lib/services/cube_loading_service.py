class CubeLoadingService(object):
    def __init__(self, cube_axes_service, cube_metadata_service, iris_wrapper):
        self._cube_axes_service = cube_axes_service
        self._cube_metadata_service = cube_metadata_service
        self._iris_wrapper = iris_wrapper

    def load_file(self, filename, cube_selection_model):
        cubes = self._iris_wrapper.load_cubes(filename)
        cube_selection_model.cubes = cubes
        cube_selection_model.cube_index = 0
        self.load_cube(cube_selection_model)

    def load_cube(self, cube_selection_model):
        cube = cube_selection_model.selected_cube()
        self._cube_axes_service.populate_major_axes(cube)
        self._cube_axes_service.populate_minor_axes(cube)
        self._cube_metadata_service.populate_metadata(cube)
