from thea.lib.models.cube_selection_model import get_cube_selection_model
from thea.lib.models.plot_model import get_plot_model
from thea.lib.services.plot_service import update_plot


class UpdatePlotController(object):

    def __init__(self, cube_selection_model, plot_model):
        self._cube_selection_model = cube_selection_model
        self._plot_model = plot_model

    def update_plot(self):
        update_plot(self._cube_selection_model, self._plot_model)


_update_plot_controller = UpdatePlotController(
    get_cube_selection_model,
    get_plot_model)


def get_update_plot_controller():
    return _update_plot_controller