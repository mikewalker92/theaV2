
class PlotService(object):
    def __init__(self, quickplot_service, plot_model):
        self.quickplot_service = quickplot_service

        self.plot_model = plot_model

    def update_plot(self, cube):
        new_plot = self.quickplot_service.pcolormesh(cube)
        self.plot_model.set_current_plot(new_plot)