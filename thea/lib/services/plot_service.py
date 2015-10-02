
class PlotService(object):
    def __init__(self, quickplot_wrapper, plot_model):
        self.quickplot_wrapper = quickplot_wrapper

        self.plot_model = plot_model

    def update_plot(self, cube):
        new_plot = self.quickplot_wrapper.pcolormesh(cube)
        self.plot_model.set_current_plot(new_plot)