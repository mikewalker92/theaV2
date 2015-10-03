class SwitchCubeController(object):
    def __init__(self, cube_loading_service, plot_service, cube_selection_model, plot_model):
        self._cube_loading_service = cube_loading_service
        self._plot_service = plot_service
        self._cube_selection_model = cube_selection_model
        self._plot_model = plot_model

    def load_file(self, filename):
        self._cube_loading_service.load_cubes(filename, self._cube_selection_model)
        self._plot_service.update_plot(self._cube_selection_model, self._plot_model)
