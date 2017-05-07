from datetime import datetime
from PySide import QtGui
import sys
import time

app = QtGui.QApplication(sys.argv)

import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4'] = 'PySide'

import unittest
from thea.lib.controllers.new_cube_controller import get_new_cube_controller
from thea.lib.helpers.view_helper_functions import get_all_item_names
from thea.lib.views.main_window import get_main_window
from thea.lib.views.selection.user_selection_widget import UserSelectionWidget
from thea.lib.views.selection.slice.select_cube_widget import SelectCubeWidget
from thea.lib.views.selection.slice.collapsed_dimension_widget import CollapsedDimensionWidget
from thea.lib.views.selection.slice.axes_widget import AxesWidget


class IntegrationBase(unittest.TestCase):
    MAX_WEIGHT_SECONDS = 15

    @classmethod
    def setUpClass(cls):
        # Start the application
        get_main_window()

    def setUp(self):
        self.__initial_figure = self.__get_current_figure()

    @classmethod
    def tearDownClass(cls):
        get_main_window().close()

    def __get_user_selection_widget(self):
        """
        :rtype: UserSelectionWidget
        """
        return get_main_window()._central_widget._user_selection_widget

    def __get_collapsed_dimensions_widget(self):
        """
        :rtype: CollapsedDimensionWidget
        """
        return self.__get_user_selection_widget()._slice_selection_widget._collapsed_dimensions_widget

    def __get_cube_selection_widget(self):
        """
        :rtype: SelectCubeWidget
        """
        return self.__get_user_selection_widget()._slice_selection_widget._select_cube_widget

    def __get_axes_widget(self):
        """
        :rtype: AxesWidget
        """
        return self.__get_user_selection_widget()._slice_selection_widget._axes_widget

    def __get_current_figure(self):
        return get_main_window()._central_widget._matplotlib_widget._canvas.figure

    # Actions
    def _load_file(self, filename):
        get_new_cube_controller().open_file(filename)

    # Assertions
    def _assert_cube_name_is(self, expected_name):
        actual_name = self.__get_cube_selection_widget()._cube_selection_combo.currentText()
        self.assertEqual(
            expected_name,
            actual_name,
            "Expected the current cube to be named '{0}', but found '{1}'".format(expected_name, actual_name)
        )

    def _assert_all_cubes_are(self, expected_names):
        combo_box = self.__get_cube_selection_widget()._cube_selection_combo
        actual_names = get_all_item_names(combo_box)
        self.assertEqual(
            expected_names,
            actual_names,
            "Expected list of cubes to be '{0}', but found '{1}'".format(expected_names, actual_names)
        )

    def _assert_x_axis_is(self, expected_name):
        actual_name = self.__get_axes_widget()._x_axis_combo.currentText()
        self.assertEqual(
            expected_name,
            actual_name,
            "Expected the x-axis to be named '{0}', but found '{1}'".format(expected_name, actual_name)
        )

    def _assert_y_axis_is(self, expected_name):
        actual_name = self.__get_axes_widget()._y_axis_combo.currentText()
        self.assertEqual(
            expected_name,
            actual_name,
            "Expected the y-axis to be named '{0}', but found '{1}'".format(expected_name, actual_name)
        )

    def _assert_no_collapsed_dimensions(self):
        dimensions = self.__get_collapsed_dimensions_widget()._collapsed_dimensions
        self.assertFalse(
            dimensions,
            "Expected there to be no collapsed dimensions, but found '{0}'".format(dimensions)
        )

    def _assert_cube_readout_contains(self, term):
        pass

    def _assert_slice_readout_contains(self, term):
        pass

    def _assert_slice_data_exists(self):
        pass

    def _wait_for_figure_to_update(self):
        start_of_wait = datetime.now()

        while self.__initial_figure == self.__get_current_figure():
            if (datetime.now() - start_of_wait).seconds > self.MAX_WEIGHT_SECONDS:
                self.fail('Expected figure to be updated, but it was not')
            time.sleep(1)

        # continue