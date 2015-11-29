import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4'] = 'PySide'

from PySide import QtGui
from unittest import TestCase
from iris.cube import Cube, iris
from mockito import mock, when
import sys
from thea.test.integration.integration_test_config import IntegrationTestConfig


cube_location = "test-cubes.pp"
two_dimensional_test_cube = Cube([
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1]])


class TestIntegration(TestCase):

    test_cubes = iris.load_cubes(cube_location)

    # controllers
    switch_cube_controller = None
    plot_controller = None

    # helpers
    iris_wrapper = None
    quickplot_wrapper = None
    cube_collapser = None
    renderer = None

    # models
    plot_model = None
    cube_selection_model = None

    @classmethod
    def setUpClass(cls, ):
        # Create a QApplication to run the tests in.
        app = QtGui.QApplication(sys.argv)

        iris.save(two_dimensional_test_cube, cube_location)

    def setUp(self):
        test_config = IntegrationTestConfig()

        # Start the app by creating the main window.
        self._main_window = test_config.get_main_window()

        self.renderer = test_config.get_renderer()

        self.switch_cube_controller = test_config.get_switch_cube_controller()
        self.plot_controller = test_config.get_plot_controller()

        self.iris_wrapper = test_config.get_iris_wrapper()
        self.quickplot_wrapper = test_config.get_quickplot_wrapper()
        self.cube_collapser = test_config.get_cube_collapser()

        self.plot_model = test_config.get_plot_model()
        self.cube_selection_model = test_config.get_cube_selection_model()

    def test_filename_openFile_loadsFileAndCreatesPlot(self):
        # Given
        new_plot = mock()
        when(self.quickplot_wrapper.pcolormesh(two_dimensional_test_cube)).thenReturn(new_plot)

        # When
        self.switch_cube_controller.load_file(cube_location)

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

    def tearDown(self):
        self.renderer.reset()