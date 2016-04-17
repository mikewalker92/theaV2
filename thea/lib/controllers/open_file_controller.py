from thea.lib.helpers.model_utils import clear_models
from thea.lib.models.view_model import get_view_model
from thea.lib.services.load_file_service import load_file
from thea.lib.services.populate_view_service import populate_view
from thea.lib.services.update_plot_service import update_plot


class OpenFileController(object):
    def __init__(self, view_model):
        """
        :type view_model: thea.lib.models.view_model.ViewModel
        """
        self._options = view_model.options
        self._information = view_model.information
        self._plot = view_model.plot

    def open_file(self, filename):
        """
        :type filename: str
        """
        clear_models([self._options, self._information, self._plot])

        load_file(filename, self._options)

        # select the first cube.
        self._options.cube_index = 0
        populate_view(self._options, self._information)

        update_plot(self._plot, self._options)


_open_file_controller = OpenFileController(get_view_model())


def get_open_file_controller():
    """
    :rtype: OpenFileController
    """
    return _open_file_controller