"""
Entry point to Thea.
"""
import getopt

import sys

from PySide import QtGui
app = QtGui.QApplication(sys.argv)

import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4'] = 'PySide'

from thea.lib.config.properties import properties
from thea.lib.controllers.open_file_controller import get_open_file_controller
from thea.lib.views.main_window import get_main_window

import os.path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main(input_args):
    filename = None
    render_ui = True

    try:
        options, _ = getopt.getopt(input_args, "f:", ["file=", "mock-renderer"])
    except getopt.GetoptError:
        print "usage: -f <filename> --file<filename> --mock-renderer"
        sys.exit(2)

    for option, argument in options:
        if option == "-f":
            filename = argument
        elif option == "--file":
            filename = argument
        elif option == "--mock-renderer":
            render_ui = False

    properties().render_ui = render_ui

    # start the app by creating the main window.
    get_main_window()

    if filename is not None:
        get_open_file_controller().open_file(filename)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv[1:])