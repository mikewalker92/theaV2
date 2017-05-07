from PySide import QtGui
import sys

app = QtGui.QApplication(sys.argv)

import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4'] = 'PySide'

import unittest
from thea.lib.controllers.new_cube_controller import get_new_cube_controller
from thea.lib.helpers.view_helper_functions import get_all_item_names
from thea.lib.views.main_window import get_main_window
from thea.lib.views.selection.slice.select_cube_widget import SelectCubeWidget


class IntegrationBase(unittest.TestCase):

    def setUp(self):
        self.__main_window = get_main_window()

    def tearDown(self):
        self.__main_window.close()

    def __get_cube_selection_widget(self):
        """
        :rtype: SelectCubeWidget
        """
        return self.__main_window._central_widget._user_selection_widget._slice_selection_widget._select_cube_widget

    # Actions
    def _load_file(self, filename):
        get_new_cube_controller().open_file(filename)

    # Assertions
    def _assert_cube_name_is(self, expected_name):
        actual_name = self.__get_cube_selection_widget()._cube_selection_combo.currentText()
        self.assertEqual(
            expected_name,
            actual_name,
            'Expected the current cube to be named {0}, but found {1}'.format(expected_name, actual_name)
        )

    def _assert_all_cubes_are(self, expected_names):
        combo_box = self.__get_cube_selection_widget()._cube_selection_combo
        actual_names = get_all_item_names(combo_box)
        self.assertEqual(
            expected_names,
            actual_names,
            'Expected list of cubes to be {0}, but found {1}'.format(expected_names, actual_names)
        )

    def _assert_x_axis_is(self, axis_name):
        pass

    def _assert_y_axis_is(self, axis_name):
        pass

    def _assert_no_collapsed_dimensions(self):
        pass

    def _assert_cube_readout_contains(self, term):
        pass

    def _assert_slice_readout_contains(self, term):
        pass

    def _assert_slice_data_exists(self):
        pass

    def _assert_figure_has_been_plotted(self):
        pass