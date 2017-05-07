from thea.test.integration.integration_base import IntegrationBase


class LoadFileIntegrationTest(IntegrationBase):

    def test_load_single_2d_cube(self):
        # When
        self._load_file('resources/single_2d_cube.pp')

        # Then
        self._assert_cube_name_is('cube name')
        self._assert_all_cubes_are(['cube name'])
        self._assert_x_axis_is('latitude')
        self._assert_y_axis_is('longitude')
        self._assert_no_collapsed_dimensions()

        self._assert_cube_readout_contains('cube name')
        self._assert_slice_readout_contains('cube name')
        self._assert_slice_data_exists()

        self._assert_figure_has_been_plotted()