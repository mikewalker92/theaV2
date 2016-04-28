from thea.lib.models.view_model import get_view_model
from thea.lib.services.populate_view_service import populate_view
from thea.lib.services.update_plot_service import update_plot


class SwitchCubeController(object):
    def __init__(self, view_model):
        """
        :type view_model: thea.lib.models.view_model.ViewModel
        """
        self._view_model = view_model

    def switch_cube(self):
        self._view_model.clear()
        populate_view(self._view_model)
        update_plot(self._view_model)


_switch_cube_controller = SwitchCubeController(get_view_model())


def get_switch_cube_controller():
    """
    :rtype: SwitchCubeController
    """
    return _switch_cube_controller
