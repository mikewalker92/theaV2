from unittest import TestCase
from iris.cube import Cube
from mockito import mock, when, verify
from thea.lib.helpers.iris_wrapper import IrisWrapper
from thea.lib.models.cube_selection_model import CubeSelectionModel
from thea.lib.services.cube_loading_service import CubeLoadingService


class TestCubeLoadingService(TestCase):

    cube_loading_service = None

    mock_iris_wrapper = mock(IrisWrapper)
    cube_selection_model = None

    def setUp(self):
        self.cube_selection_model = CubeSelectionModel()
        self.cube_loading_service = CubeLoadingService(self.mock_iris_wrapper)

    def test_filename_when_loadCubes_getsCubeAndUpdatesPlot(self):
        # Given
        filename = "path/to/cubes"
        cubes = [mock(Cube)]
        when(self.mock_iris_wrapper).load_cubes(filename).thenReturn(cubes)

        # When
        self.cube_loading_service.load_cubes(filename, self.cube_selection_model)

        # Then
        self.assertEqual(cubes, self.cube_selection_model.cubes)