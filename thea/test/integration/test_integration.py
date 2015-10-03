from unittest import TestCase
from iris.cube import Cube
from mockito import mock, when
from thea.test.integration.application_test_config import TestConfig


class TestIntegration(TestCase):

    # controllers
    switch_cube_controller = None
    plot_controller = None

    # helpers
    iris_wrapper = None
    quickplot_wrapper = None
    cube_collapser = None

    # models
    plot_model = None
    cube_selection_model = None

    def setUp(self):
        test_config = TestConfig()

        self.switch_cube_controller = test_config.get_switch_cube_controller()
        self.plot_controller = test_config.get_plot_controller()

        self.iris_wrapper = test_config.get_iris_wrapper()
        self.quickplot_wrapper = test_config.get_quickplot_wrapper()
        self.cube_collapser = test_config.get_cube_collapser()

        self.plot_model = test_config.get_plot_model()
        self.cube_selection_model = test_config.get_cube_selection_model()

    def test_filename_openFile_loadsFileAndCreatesPlot(self):
        # Given
        filename = "path/to/cubes"
        new_plot = mock()
        cube = mock(Cube)
        cubes = [cube]

        when(self.iris_wrapper).load_cubes(filename).thenReturn(cubes)
        when(self.quickplot_wrapper).pcolormesh(cube).thenReturn(new_plot)

        # When
        self.switch_cube_controller.load_file(filename)

        # Then
        self.assertEqual(new_plot, self.plot_model.current_plot)

    def test_plotModel_updatePlot_plotIsUpdated(self):
        # Given
        updated_plot = mock()
        cube = mock(Cube)
        cubes = [cube]
        self.cube_selection_model.cubes = cubes
        when(self.quickplot_wrapper).pcolormesh(cube).thenReturn(updated_plot)

        # When
        self.plot_controller.update_plot()

        # Then
        self.assertEqual(updated_plot, self.plot_model.current_plot)