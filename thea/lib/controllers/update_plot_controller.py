from thea.lib.helpers.model_provider import get_model_provider
from thea.lib.services.update_plot_service import update_plot


class UpdatePlotController(object):

    def __init__(self, model_provider):
        """
        :type model_provider: thea.lib.helpers.model_provider.ModelProvider
        """
        self._options_model = model_provider.options_model
        self._plot_model = model_provider.plot_model

    def update_plot(self):
        update_plot(self._plot_model, self._options_model)


_update_plot_controller = UpdatePlotController(get_model_provider())


def get_update_plot_controller():
    """
    :rtype: UpdatePlotController
    """
    return _update_plot_controller