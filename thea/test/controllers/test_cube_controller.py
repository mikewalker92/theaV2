from unittest import TestCase
from mockito import mock, when, verify
from thea.lib.controllers.cube_controller import CubeController
from thea.lib.services.cube_loading_service import CubeLoadingService


class CubeControllerTests(TestCase):

    mock_cube_loading_service = None
    cube_controller = None

    def setUp(self):
        self.mock_cube_loading_service = mock(CubeLoadingService)
        self.cube_controller = CubeController(self.mock_cube_loading_service)

    def test_filename_loadCubes_callsServiceWithCorrectParams(self):
        # Given
        filename = "path/to/cube.pp"

        # When
        self.cube_controller.load_cubes(filename)

        # Then
        verify(self.mock_cube_loading_service).load_cubes(filename)
