"""
Entry point to Thea.
"""
import getopt

import sys

from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

import matplotlib
matplotlib.use('Qt5Agg')

from thea.lib.controllers.new_cube_controller import get_new_cube_controller
from thea.lib.views.main_window import get_main_window

import os.path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main(input_args):
    filename = None

    try:
        options, _ = getopt.getopt(input_args, "f:", ["file="])
    except getopt.GetoptError:
        print("usage: -f <filename> --file<filename>")
        sys.exit(2)

    for option, argument in options:
        if option == "-f":
            filename = argument
        elif option == "--file":
            filename = argument

    # start the app by creating the main window.
    get_main_window()

    if filename is not None:
        get_new_cube_controller().open_file(filename)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv[1:])