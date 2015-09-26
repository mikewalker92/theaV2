class PlotController(object):

    def __init__(self, plot_service, cube_selection_model, cube_collapser):
        self._plot_service = plot_service
        self._cube_selection_model = cube_selection_model
        self._cube_collapser = cube_collapser

    def update_plot(self):
        cube_to_plot = self._cube_collapser.collapse_cube(self._cube_selection_model)
        self._plot_service.update_plot(cube_to_plot)