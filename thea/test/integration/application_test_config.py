from mockito import mock
from thea.lib.controllers.cube_controller import CubeController
from thea.lib.controllers.plot_controller import PlotController
from thea.lib.helpers.cube_collapser import CubeCollapser
from thea.lib.helpers.iris_wrapper import IrisWrapper
from thea.lib.helpers.quickplot_wrapper import QuickplotWrapper
from thea.lib.models.cube_selection_model import CubeSelectionModel
from thea.lib.models.plot_model import PlotModel
from thea.lib.services.cube_loading_service import CubeLoadingService
from thea.lib.services.plot_service import PlotService


class TestConfig(object):
    """
    Class to instantiate objects with their required dependencies.
    """

    def __init__(self):
        # Helpers
        self._cube_collapser = CubeCollapser()
        self._quickplot_wrapper = mock(QuickplotWrapper)
        self._iris_wrapper = mock(IrisWrapper)

        # Models
        self._plot_model = PlotModel()
        self._cube_selection_model = CubeSelectionModel()

        # Services
        self._plot_service = PlotService(
            self.get_quickplot_wrapper(),
            self.get_plot_model())

        self._cube_loading_service = CubeLoadingService(
            self.get_iris_wrapper(),
            self.get_plot_service(),
            self.get_cube_selection_model())

        # Controllers
        self._plot_controller = PlotController(
            self.get_plot_service(),
            self.get_cube_selection_model(),
            self.get_cube_collapser())

        self._cube_controller = CubeController(
            self.get_cube_loading_service())

    """
    Helpers
    """
    def get_cube_collapser(self):
        return self._cube_collapser

    def get_quickplot_wrapper(self):
        return self._quickplot_wrapper

    def get_iris_wrapper(self):
        return self._iris_wrapper

    """
    Models
    """
    def get_plot_model(self):
        return self._plot_model

    def get_cube_selection_model(self):
        return self._cube_selection_model

    """
    Services
    """
    def get_plot_service(self):
        return self._plot_service

    def get_cube_loading_service(self):
        return self._cube_loading_service

    """
    Controllers
    """
    def get_plot_controller(self):
        return self._plot_controller

    def get_cube_controller(self):
        return self._cube_controller

    """
    Views
    """
    # No views are require for the integration tests.