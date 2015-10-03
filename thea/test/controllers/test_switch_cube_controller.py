from unittest import TestCase
from mockito import mock, verify
from thea.lib.controllers.switch_cube_controller import SwitchCubeController
from thea.lib.models.cube_selection_model import CubeSelectionModel
from thea.lib.models.plot_model import PlotModel
from thea.lib.services.cube_loading_service import CubeLoadingService
from thea.lib.services.plot_service import PlotService


class SwitchCubeControllerTests(TestCase):

    mock_cube_loading_service = None
    mock_plot_service = None
    switch_cube_controller = None

    def setUp(self):
        self.mock_cube_loading_service = mock(CubeLoadingService)
        self.mock_plot_service = mock(PlotService)
        self.mock_cube_selection_model = mock(CubeSelectionModel)
        self.mock_plot_model = mock(PlotModel)

        self.switch_cube_controller = SwitchCubeController(
            self.mock_cube_loading_service,
            self.mock_plot_service,
            self.mock_cube_selection_model,
            self.mock_plot_model)

    def test_filename_loadCubes_callsServiceWithCorrectParams(self):
        # Given
        filename = "path/to/cube.pp"

        # When
        self.switch_cube_controller.load_file(filename)

        # Then
        verify(self.mock_cube_loading_service).load_cubes(filename, self.mock_cube_selection_model)
        verify(self.mock_plot_service).update_plot(self.mock_cube_selection_model, self.mock_plot_model)
