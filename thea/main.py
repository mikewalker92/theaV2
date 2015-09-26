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

    _ = ApplicationConfig()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()