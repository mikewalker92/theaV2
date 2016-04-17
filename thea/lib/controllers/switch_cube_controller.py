from thea.lib.helpers.model_utils import clear_models
from thea.lib.models.view_model import get_view_model
from thea.lib.services.populate_view_service import populate_view
from thea.lib.services.update_plot_service import update_plot


class SwitchCubeController(object):
    def __init__(self, view_model):
        """
        :type view_model: thea.lib.models.view_model.ViewModel
        """
        self._information = view_model.information
        self._plot = view_model.plot
        self._options = view_model.options

    def switch_cube(self):
        clear_models([self._information, self._plot, self._options])
        populate_view(self._options, self._information)
        update_plot(self._plot, self._options)


_switch_cube_controller = SwitchCubeController(get_view_model())


def get_switch_cube_controller():
    """
    :rtype: SwitchCubeController
    """
    return _switch_cube_controller
