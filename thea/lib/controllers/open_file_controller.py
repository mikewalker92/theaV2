from thea.lib.models.view_model import get_view_model
from thea.lib.services.load_file_service import load_file
from thea.lib.services.populate_view_service import populate_view
from thea.lib.services.update_plot_service import update_plot


class OpenFileController(object):
    def __init__(self, view_model):
        """
        :type view_model: thea.lib.models.view_model.ViewModel
        """
        self._view_model = view_model

    def open_file(self, filename):
        """
        :type filename: str
        """
        self._view_model.clear()

        load_file(filename, self._view_model.options.cube_options)
        populate_view(self._view_model)
        update_plot(self._view_model)


_open_file_controller = OpenFileController(get_view_model())


def get_open_file_controller():
    """
    :rtype: OpenFileController
    """
    return _open_file_controller