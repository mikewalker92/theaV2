from thea.lib.models.cube_selection_model import get_cube_selection_model
from thea.lib.models.plot_model import get_plot_model
from thea.lib.services.cube_loading_service import load_file
from thea.lib.services.plot_service import update_plot


class SwitchCubeController(object):
    def __init__(self, cube_selection_model, plot_model):
        self._cube_selection_model = cube_selection_model
        self._plot_model = plot_model

    def open_file(self, filename):
        cubes = load_file(filename)




    def load_file(self, filename):
        load_file(filename, self._cube_selection_model)
        update_plot(self._cube_selection_model, self._plot_model)

    def load_cube(self):
        pass


_switch_cube_controller = SwitchCubeController(
    get_cube_selection_model(),
    get_plot_model())


def get_switch_cube_controller():
    return _switch_cube_controller
