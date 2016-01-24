from thea.lib.helpers.model_provider import get_model_provider
from thea.lib.helpers.model_utils import clear_models
from thea.lib.services.populate_view_service import populate_view
from thea.lib.services.update_plot_service import update_plot


class SwitchCubeController(object):
    def __init__(self, model_provider):
        self._information_model = model_provider.information_model
        self._plot_model = model_provider.plot_model
        self._options_model = model_provider.options_model

    def switch_cube(self):
        clear_models([self._information_model, self._plot_model, self._options_model])
        populate_view(self._options_model, self._information_model)
        update_plot(self._plot_model, self._options_model)


_switch_cube_controller = SwitchCubeController(get_model_provider())


def get_switch_cube_controller():
    return _switch_cube_controller
