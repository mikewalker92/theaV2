from unittest import TestCase
from iris.cube import Cube
from mockito import mock, when, verify
from thea.lib.helpers.iris_wrapper import IrisWrapper
from thea.lib.models.cube_selection_model import CubeSelectionModel
from thea.lib.services.cube_axes_service import CubeAxesService
from thea.lib.services.cube_loading_service import CubeLoadingService
from thea.lib.services.cube_metadata_service import CubeMetadataService


class TestCubeLoadingService(TestCase):

    cube_loading_service = None

    mock_cube_axes_service = None
    mock_cube_metadata_service = None
    mock_iris_wrapper = None
    mock_cube = None
    cube_selection_model = None

    def setUp(self):
        self.mock_cube_axes_service = mock(CubeAxesService)
        self.mock_cube_metadata_service = mock(CubeMetadataService)
        self.mock_iris_wrapper = mock(IrisWrapper)
        self.mock_cube = mock(Cube)

        self.cube_selection_model = CubeSelectionModel()
        self.cube_selection_model.cubes.append(self.mock_cube)

        self.cube_loading_service = CubeLoadingService(
            self.mock_cube_axes_service,
            self.mock_cube_metadata_service,
            self.mock_iris_wrapper)

    def test_filename_loadFiles_getsCubeAndUpdatesPlot(self):
        # Given
        filename = "path/to/cubes"
        cubes = [self.mock_cube]
        when(self.mock_iris_wrapper).load_cubes(filename).thenReturn(cubes)

        # When
        self.cube_loading_service.load_file(filename, self.cube_selection_model)

        # Then
        self.assertEqual(cubes, self.cube_selection_model.cubes)
        self.assertEqual(0, self.cube_selection_model.cube_index)
        verify(self.mock_cube_axes_service).populate_major_axes(self.mock_cube)
        verify(self.mock_cube_axes_service).populate_minor_axes(self.mock_cube)
        verify(self.mock_cube_metadata_service).populate_metadata(self.mock_cube)

    def test_cubeSelectionModel_loadCube_populatesView(self):
        # When
        self.cube_loading_service.load_cube(self.cube_selection_model)

        # Then
        verify(self.mock_cube_axes_service).populate_major_axes(self.mock_cube)
        verify(self.mock_cube_axes_service).populate_minor_axes(self.mock_cube)
        verify(self.mock_cube_metadata_service).populate_metadata(self.mock_cube)