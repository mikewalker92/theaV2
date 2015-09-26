class CubeLoadingService(object):
    def __init__(self, iris_wrapper, plot_service, cube_selection_model):
        self._iris_wrapper = iris_wrapper
        self._plot_service = plot_service
        self._cube_selection_model = cube_selection_model

    def load_cubes(self, filename):
        cube = self._iris_wrapper.load_cubes(filename)[0]
        self._cube_selection_model.set_cube(cube)
        self._plot_service.update_plot(cube)