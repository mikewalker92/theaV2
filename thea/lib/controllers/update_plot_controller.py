from thea.lib.models.view_model import get_view_model
from thea.lib.services.update_plot_service import update_plot


class UpdatePlotController(object):

    def __init__(self, view_model):
        """
        :type view_model: thea.lib.models.view_model.ViewModel
        """
        self._options = view_model.options
        self._plot = view_model.plot

    def update_plot(self):
        update_plot(self._plot, self._options)


_update_plot_controller = UpdatePlotController(get_view_model())


def get_update_plot_controller():
    """
    :rtype: UpdatePlotController
    """
    return _update_plot_controller