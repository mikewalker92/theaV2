from thea.lib.helpers.model_provider import get_model_provider
from thea.lib.helpers.model_utils import clear_models
from thea.lib.services.load_file_service import load_file
from thea.lib.services.populate_view_service import populate_view
from thea.lib.services.update_plot_service import update_plot


class OpenFileController(object):
    def __init__(self, model_provider):
        """
        :type model_provider: thea.lib.helpers.model_provider.ModelProvider
        """
        self._options_model = model_provider.options_model
        self._information_model = model_provider.information_model
        self._plot_model = model_provider.plot_model

    def open_file(self, filename):
        """
        :type filename: str
        """
        clear_models([self._options_model, self._information_model, self._plot_model])

        load_file(filename, self._options_model)

        # select the first cube.
        self._options_model.cube_index = 0
        populate_view(self._options_model, self._information_model)

        update_plot(self._plot_model, self._options_model)


_open_file_controller = OpenFileController(get_model_provider())


def get_open_file_controller():
    """
    :rtype: OpenFileController
    """
    return _open_file_controller