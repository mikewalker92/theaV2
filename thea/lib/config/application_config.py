from thea.lib.controllers.switch_cube_controller import SwitchCubeController
from thea.lib.controllers.plot_controller import PlotController
from thea.lib.helpers.cube_collapser import CubeCollapser
from thea.lib.helpers.cube_utils import CubeUtils
from thea.lib.helpers.iris_wrapper import IrisWrapper
from thea.lib.helpers.quickplot_wrapper import QuickplotWrapper
from thea.lib.helpers.renderer import Renderer
from thea.lib.models.cube_selection_model import CubeSelectionModel
from thea.lib.models.plot_model import PlotModel
from thea.lib.services.cube_axes_service import CubeAxesService
from thea.lib.services.cube_loading_service import CubeLoadingService
from thea.lib.services.cube_metadata_service import CubeMetadataService
from thea.lib.services.plot_service import PlotService
from thea.lib.views.central_widget import CentralWidget
from thea.lib.views.cube_data_widget import CubeDataWidget
from thea.lib.views.cube_information_widget import CubeInformationWidget
from thea.lib.views.cube_viewer_widget import CubeViewerWidget
from thea.lib.views.major_axes_widget import MajorAxesWidget
from thea.lib.views.matplotlib_widget import MatplotlibWidget
from thea.lib.views.minor_axes_widget import MinorAxesWidget
from thea.lib.views.options_widget import OptionsWidget
from thea.lib.views.cube_options_widget import CubeOptionsWidget
from thea.lib.views.plot_options_widget import PlotOptionsWidget
from thea.lib.views.select_cube_widget import SelectCubeWidget
from thea.lib.views.update_plot_widget import UpdatePlotWidget
from thea.lib.views.main_window import MainWindow


class ApplicationConfig(object):
    """
    Class to instantiate objects with their required dependencies.
    """

    # Helpers
    _cube_collapser = None
    _quickplot_wrapper = None
    _iris_wrapper = None
    _renderer = None
    _cube_utils = None

    # Models
    _plot_model = None
    _cube_selection_model = None

    # Services
    _plot_service = None
    _cube_loading_service = None
    _cube_axes_service = None
    _cube_metadata_service = None

    # Controllers
    _plot_controller = None
    _switch_cube_controller = None

    # Views
    _select_cube_widget = None
    _major_axes_widget = None
    _minor_axes_widget = None
    _cube_options_widget = None
    _plot_options_widget = None
    _update_plot_widget = None
    _options_widget = None
    _matplotlib_widget = None
    _full_cube_information_widget = None
    _cube_slice_information_widget = None
    _cube_data_widget = None
    _cube_viewer_widget = None
    _central_widget = None
    _main_window = None

    """
    Helpers
    """
    def get_cube_collapser(self):
        if self._cube_collapser is None:
            self._cube_collapser = CubeCollapser()

        return self._cube_collapser

    def get_quickplot_wrapper(self):
        if self._quickplot_wrapper is None:
            self._quickplot_wrapper = QuickplotWrapper()

        return self._quickplot_wrapper

    def get_iris_wrapper(self):
        if self._iris_wrapper is None:
            self._iris_wrapper = IrisWrapper()

        return self._iris_wrapper

    def get_renderer(self):
        if self._renderer is None:
            self._renderer = Renderer()

        return self._renderer

    def get_cube_utils(self):
        if self._cube_utils is None:
            self._cube_utils = CubeUtils(
                self.get_iris_wrapper())

        return self._cube_utils

    """
    Models
    """
    def get_plot_model(self):
        if self._plot_model is None:
            self._plot_model = PlotModel()

        return self._plot_model

    def get_cube_selection_model(self):
        if self._cube_selection_model is None:
            self._cube_selection_model = CubeSelectionModel()

        return self._cube_selection_model

    """
    Services
    """
    def get_plot_service(self):
        if self._plot_service is None:
            self._plot_service = PlotService(
                self.get_quickplot_wrapper())

        return self._plot_service

    def get_cube_loading_service(self):
        if self._cube_loading_service is None:
            self._cube_loading_service = CubeLoadingService(
                self.get_cube_axes_service(),
                self.get_cube_metadata_service(),
                self.get_iris_wrapper())

        return self._cube_loading_service

    def get_cube_axes_service(self):
        if self._cube_axes_service is None:
            self._cube_axes_service = CubeAxesService()

        return self._cube_axes_service

    def get_cube_metadata_service(self):
        if self._cube_metadata_service is None:
            self._cube_metadata_service = CubeMetadataService()

        return self._cube_metadata_service

    """
    Controllers
    """
    def get_plot_controller(self):
        if self._plot_controller is None:
            self._plot_controller = PlotController(
                self.get_plot_service(),
                self.get_cube_selection_model(),
                self.get_plot_model())

        return self._plot_controller

    def get_switch_cube_controller(self):
        if self._switch_cube_controller is None:
            self._switch_cube_controller = SwitchCubeController(
                self.get_cube_loading_service(),
                self.get_plot_service(),
                self.get_cube_selection_model(),
                self.get_plot_model())

        return self._switch_cube_controller

    """
    Views
    """
    def get_matplotlib_widget(self):
        if self._matplotlib_widget is None:
            self._matplotlib_widget = MatplotlibWidget(
                self.get_renderer(),
                self.get_plot_model())

        return self._matplotlib_widget

    def get_full_cube_information_widget(self):
        if self._full_cube_information_widget is None:
            self._full_cube_information_widget = CubeInformationWidget(
                self.get_renderer())

        return self._full_cube_information_widget

    def get_cube_slice_information_widget(self):
        if self._cube_slice_information_widget is None:
            self._cube_slice_information_widget = CubeInformationWidget(
                self.get_renderer())

        return self._cube_slice_information_widget

    def get_cube_data_widget(self):
        if self._cube_data_widget is None:
            self._cube_data_widget = CubeDataWidget(
                self.get_renderer())

        return self._cube_data_widget

    def get_cube_options_widget(self):
        if self._cube_options_widget is None:
            self._cube_options_widget = CubeOptionsWidget(
                self.get_renderer(),
                self.get_select_cube_widget(),
                self.get_major_axes_widget(),
                self.get_minor_axes_widget(),)

        return self._cube_options_widget

    def get_plot_options_widget(self):
        if self._plot_options_widget is None:
            self._plot_options_widget = PlotOptionsWidget(
                self.get_renderer())

        return self._plot_options_widget

    def get_select_cube_widget(self):
        if self._select_cube_widget is None:
            self._select_cube_widget = SelectCubeWidget(
                self.get_renderer(),
                self.get_cube_selection_model(),
                self.get_cube_utils())

        return self._select_cube_widget

    def get_major_axes_widget(self):
        if self._major_axes_widget is None:
            self._major_axes_widget = MajorAxesWidget(
                self.get_renderer())

        return self._major_axes_widget

    def get_minor_axes_widget(self):
        if self._minor_axes_widget is None:
            self._minor_axes_widget = MinorAxesWidget(
                self.get_renderer())

        return self._minor_axes_widget

    def get_cube_viewer_widget(self):
        if self._cube_viewer_widget is None:
            self._cube_viewer_widget = CubeViewerWidget(
                self.get_renderer(),
                self.get_full_cube_information_widget(),
                self.get_cube_slice_information_widget(),
                self.get_cube_data_widget())

        return self._cube_viewer_widget

    def get_update_plot_widget(self):
        if self._update_plot_widget is None:
            self._update_plot_widget = UpdatePlotWidget(
                self.get_renderer(),
                self.get_plot_controller())

        return self._update_plot_widget

    def get_options_widget(self):
        if self._options_widget is None:
            self._options_widget = OptionsWidget(
                self.get_renderer(),
                self.get_cube_options_widget(),
                self.get_plot_options_widget(),
                self.get_update_plot_widget())

        return self._options_widget

    def get_central_widget(self):
        if self._central_widget is None:
            self._central_widget = CentralWidget(
                self.get_renderer(),
                self.get_matplotlib_widget(),
                self.get_cube_viewer_widget(),
                self.get_options_widget())

        return self._central_widget

    def get_main_window(self):
        if self._main_window is None:
            self._main_window = MainWindow(
                self.get_renderer(),
                self.get_central_widget(),
                self.get_switch_cube_controller())

        return self._main_window
