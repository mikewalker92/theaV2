from unittest import TestCase
from iris.cube import Cube
from mockito import mock, when, verify
from thea.lib.helpers.iris_wrapper import IrisWrapper
from thea.lib.models.cube_selection_model import CubeSelectionModel
from thea.lib.services.cube_loading_service import CubeLoadingService
from thea.lib.services.plot_service import PlotService


class TestCubeLoadingService(TestCase):

    cube_loading_service = None

    mock_iris_wrapper = mock(IrisWrapper)
    mock_plot_service = mock(PlotService)
    mock_cube_selection_model = mock(CubeSelectionModel)

    def setUp(self):
        self.cube_loading_service = CubeLoadingService(
            self.mock_iris_wrapper,
            self.mock_plot_service,
            self.mock_cube_selection_model)

    def test_filename_when_loadCubes_getsCubeAndUpdatesPlot(self):
        # Given
        filename = "path/to/cubes"
        cube = mock(Cube)
        cubes = [cube]
        when(self.mock_iris_wrapper).load_cubes(filename).thenReturn(cubes)

        # When
        self.cube_loading_service.load_cubes(filename)

        # Then
        verify(self.mock_cube_selection_model).set_cube(cube)
        verify(self.mock_plot_service).update_plot(cube)