from unittest import TestCase
from iris.cube import Cube
from mockito import mock, verify, when
from thea.lib.controllers.plot_controller import PlotController
from thea.lib.helpers.cube_collapser import CubeCollapser
from thea.lib.models.cube_selection_model import CubeSelectionModel
from thea.lib.services.plot_service import PlotService


class PlotControllerTests(TestCase):

    plot_controller = None
    mock_plot_service = mock(PlotService)
    mock_cube_selection_model = mock(CubeSelectionModel)
    mock_cube_collapser = mock(CubeCollapser)

    def setUp(self):
        self.plot_controller = PlotController(
            self.mock_plot_service,
            self.mock_cube_selection_model,
            self.mock_cube_collapser)

    def test_cubeSelectionModel_updatePlot_callsPlotService(self):
        # Given
        cube_to_plot = mock(Cube)
        when(self.mock_cube_collapser).collapse_cube(self.mock_cube_selection_model).thenReturn(cube_to_plot)

        # When
        self.plot_controller.update_plot()

        # Then
        verify(self.mock_plot_service).update_plot(cube_to_plot)
