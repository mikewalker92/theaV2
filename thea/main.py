"""
Entry point to Thea.
"""

import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4'] = 'PySide'

import warnings
# We wish to reduce output to the terminal when the program is running.
from thea.lib.config.application_config import ApplicationConfig

warnings.filterwarnings("ignore")

import os.path
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PySide import QtGui


def main():
    app = QtGui.QApplication(sys.argv)
    application_config = ApplicationConfig()

    try:
        _, initial_filename = sys.argv
        application_config.get_cube_loading_service().load_cubes(initial_filename)
    except ValueError:
        # If initial_filename is not set, nothing needs to be done.
        pass

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()