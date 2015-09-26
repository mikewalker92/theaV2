from thea.lib.controllers.cube_controller import CubeController
from thea.lib.controllers.plot_controller import PlotController
from thea.lib.helpers.cube_collapser import CubeCollapser
from thea.lib.helpers.iris_wrapper import IrisWrapper
from thea.lib.helpers.quickplot_wrapper import QuickplotWrapper
from thea.lib.models.cube_selection_model import CubeSelectionModel
from thea.lib.models.plot_model import PlotModel
from thea.lib.services.cube_loading_service import CubeLoadingService
from thea.lib.services.plot_service import PlotService
from thea.lib.views.central_widget import CentralWidget
from thea.lib.views.cube_data_widget import CubeDataWidget
from thea.lib.views.cube_information_widget import CubeInformationWidget
from thea.lib.views.cube_viewer_widget import CubeViewerWidget
from thea.lib.views.major_axes_widget import MajorAxesWidget
from thea.lib.views.matplotlib_widget import MatplotlibWidget
from thea.lib.views.minor_axes_widget import MinorAxesWidget
from thea.lib.views.options_widget import OptionsWidget
from thea.lib.views.select_cube_widget import SelectCubeWidget
from thea.lib.views.update_plot_widget import UpdatePlotWidget
from thea.lib.views.main_window import MainWindow


class ApplicationConfig(object):
    """
    Class to instantiate objects with their required dependencies.
    """

    def __init__(self):
        # Helpers
        self._cube_collapser = CubeCollapser()
        self._quickplot_wrapper = QuickplotWrapper()
        self._iris_wrapper = IrisWrapper()

        # Models
        self._plot_model = PlotModel()
        self._cube_selection_model = CubeSelectionModel()

        # Services
        self._plot_service = PlotService(
            self.get_quickplot_helper(),
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

        # Views
        self._matplotlib_widget = MatplotlibWidget(
            self.get_plot_model())

        self._full_cube_information_widget = CubeInformationWidget()
        self._cube_slice_information_widget = CubeInformationWidget()
        self._cube_data_widget = CubeDataWidget()
        self._select_cube_widget = SelectCubeWidget()
        self._major_axes_widget = MajorAxesWidget()
        self._minor_axes_widget = MinorAxesWidget()

        self._cube_viewer_widget = CubeViewerWidget(
            self.get_full_cube_information_widget(),
            self.get_cube_slice_information_widget(),
            self.get_cube_data_widget())

        self._update_plot_widget = UpdatePlotWidget(
            self.get_plot_controller())

        self._options_widget = OptionsWidget(
            self.get_select_cube_widget(),
            self.get_major_axes_widget(),
            self.get_minor_axes_widget(),
            self.get_update_plot_widget())

        self._central_widget = CentralWidget(
            self.get_matplotlib_widget(),
            self.get_cube_viewer_widget(),
            self.get_options_widget())

        self._main_window = MainWindow(
            self.get_central_widget(),
            self.get_cube_controller())

    """
    Helpers
    """
    def get_cube_collapser(self):
        return self._cube_collapser

    def get_quickplot_helper(self):
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
    def get_matplotlib_widget(self):
        return self._matplotlib_widget

    def get_full_cube_information_widget(self):
        return self._full_cube_information_widget

    def get_cube_slice_information_widget(self):
        return self._cube_slice_information_widget

    def get_cube_data_widget(self):
        return self._cube_data_widget

    def get_select_cube_widget(self):
        return self._select_cube_widget

    def get_major_axes_widget(self):
        return self._major_axes_widget

    def get_minor_axes_widget(self):
        return self._minor_axes_widget

    def get_cube_viewer_widget(self):
        return self._cube_viewer_widget

    def get_update_plot_widget(self):
        return self._update_plot_widget

    def get_options_widget(self):
        return self._options_widget

    def get_central_widget(self):
        return self._central_widget

    def get_main_window(self):
        return self._main_window

