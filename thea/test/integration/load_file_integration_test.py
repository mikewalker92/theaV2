from thea.test.integration.integration_base import IntegrationBase


class LoadFileIntegrationTest(IntegrationBase):

    def test_load_single_2d_cube(self):
        # When
        self._load_file('resources/single_2d_cube.pp')

        # Then
        self._wait_for_figure_to_update()

        self._assert_cube_name_is('wind_speed_of_gust')
        self._assert_all_cubes_are(['wind_speed_of_gust'])
        self._assert_x_axis_is('grid_latitude')
        self._assert_y_axis_is('grid_longitude')
        self._assert_no_collapsed_dimensions()

        self._assert_cube_readout_contains('wind_speed_of_gust / (m s-1)')
        self._assert_slice_readout_contains('wind_speed_of_gust / (m s-1)')
        self._assert_slice_data_is_displayed_in_table(expected_row_count=360, expected_column_count=288)
