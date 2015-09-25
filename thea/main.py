"""
Entry point thea.
"""

import warnings
# We wish to reduce output to the terminal when the program is running.
from thea.lib.controllers.main_controller import MainController
from thea.lib.services.main_service import MainService
from thea.lib.services.plot_service import PlotService

warnings.filterwarnings("ignore")

import os.path
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PySide import QtGui

import thea.lib.views.main_window as main_window


def main():
    app = QtGui.QApplication(sys.argv)

    plot_service = PlotService()
    main_service = MainService(plot_service)
    main_controller = MainController(main_service)

    _ = main_window.MainWindow(main_controller)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()