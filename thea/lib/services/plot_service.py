
class PlotService(object):
    def __init__(self, quickplot_wrapper):
        self._quickplot_wrapper = quickplot_wrapper

    def update_plot(self, cube_selection_model, plot_model):
        cube = cube_selection_model.selected_cube()

        new_plot = self._quickplot_wrapper.pcolormesh(cube)
        plot_model.current_plot = new_plot