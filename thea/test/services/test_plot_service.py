from unittest import TestCase
from iris.cube import Cube
from mockito import mock, when
from thea.lib.helpers.plotting_utils import QuickplotWrapper
from thea.lib.models.cube_selection_model import CubeSelectionModel
from thea.lib.models.plot_model import PlotModel
from thea.lib.services.plot_service import PlotService


class TestPlotService(TestCase):

    def setUp(self):
        self.mock_quickplot_wrapper = mock(QuickplotWrapper)
        self.mock_cube_selection_model = mock(CubeSelectionModel)
        self.plot_model = PlotModel()
        self.plot_service = PlotService(self.mock_quickplot_wrapper)

    def test_cube_updatePlot_setsCurrentPlot(self):
        # Given
        cube = mock(Cube)
        new_plot = mock()
        when(self.mock_cube_selection_model).selected_cube().thenReturn(cube)
        when(self.mock_quickplot_wrapper).pcolormesh(cube).thenReturn(new_plot)

        # When
        self.plot_service.update_plot(self.mock_cube_selection_model, self.plot_model)

        # Then
        self.assertEqual(new_plot, self.plot_model.current_plot)