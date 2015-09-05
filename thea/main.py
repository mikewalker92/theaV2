"""
Entry point thea.
"""

import warnings
# We wish to reduce output to the terminal when the program is running.
warnings.filterwarnings("ignore")

import os.path
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PySide import QtGui

import thea.lib.views.main_window as main_window


def main():
    app = QtGui.QApplication(sys.argv)

    _ = main_window.MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()