"""
Entry point to Thea.
"""

import matplotlib

matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4'] = 'PySide'

import warnings
# We wish to reduce output to the terminal when the program is running.

warnings.filterwarnings("ignore")

import os.path
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PySide import QtGui
app = QtGui.QApplication(sys.argv)

from thea.lib.views.main_window import get_main_window


def main():
    # start the app by creating the main window.
    main_window = get_main_window()

    try:
        _, initial_filename = sys.argv
        main_window.get_switch_cube_controller().load_file(initial_filename)
    except ValueError:
        # If initial_filename is not set, nothing needs to be done.
        # TODO - setting filename for dev purposes only
        initial_filename = '/home/mike/Programming/Scitools/iris-test-data/test_data/PP/simple_pp/global.pp'
        main_window.get_switch_cube_controller().load_file(initial_filename)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()