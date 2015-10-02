from unittest import TestCase
from iris.cube import Cube
from mockito import mock, when, verify
from thea.lib.helpers.quickplot_wrapper import QuickplotWrapper
from thea.lib.models.plot_model import PlotModel
from thea.lib.services.plot_service import PlotService


class TestPlotService(TestCase):

    plot_service = None

    mock_quickplot_wrapper = mock(QuickplotWrapper)
    mock_plot_model = mock(PlotModel)

    def setUp(self):
        self.plot_service = PlotService(
            self.mock_quickplot_wrapper,
            self.mock_plot_model)

    def test_cube_updatePlot_setsCurrentPlot(self):
        # Given
        cube = mock(Cube)
        new_plot = mock()
        when(self.mock_quickplot_wrapper).pcolormesh(cube).thenReturn(new_plot)

        # When
        self.plot_service.update_plot(cube)

        # Then
        verify(self.mock_plot_model).set_current_plot(new_plot)