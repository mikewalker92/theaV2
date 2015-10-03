class PlotController(object):

    def __init__(self, plot_service, cube_selection_model, plot_model):
        self._plot_service = plot_service
        self._cube_selection_model = cube_selection_model
        self._plot_model = plot_model

    def update_plot(self):
        self._plot_service.update_plot(self._cube_selection_model, self._plot_model)