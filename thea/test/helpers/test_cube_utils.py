from unittest import TestCase
from iris.cube import Cube
from mockito import mock, when
from thea.lib.helpers.cube_utils import CubeUtils
from thea.lib.helpers.iris_wrapper import IrisWrapper


class CubeUtilsTests(TestCase):

    def setUp(self):
        self.mock_iris_wrapper = mock(IrisWrapper)
        self.cube_utils = CubeUtils(self.mock_iris_wrapper)

    def test_listOfCubes_getNamesFromCubes_returnsListOfNames(self):
        # Given
        cube = mock(Cube)
        cubes = [cube, cube, cube]
        when(self.mock_iris_wrapper).cube_name(cube).thenReturn('cube 1').thenReturn('cube 2').thenReturn('cube 3')

        # When
        cube_names = self.cube_utils.get_names_from_cubes(cubes)

        # Then
        self.assertEqual(['cube 1', 'cube 2', 'cube 3'], cube_names)

    def test_cube_getNameFromCube_returnsCubeName(self):
        # Given
        cube = mock(Cube)
        name = 'Cube Name'
        when(self.mock_iris_wrapper).cube_name(cube).thenReturn(name)

        # When
        cube_name = self.cube_utils.get_name_from_cube(cube)

        # Then
        self.assertEqual(name, cube_name)