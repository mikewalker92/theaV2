import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4'] = 'PySide'

from PySide import QtGui
from unittest import TestCase
from iris.cube import Cube, iris
from mockito import mock, when
import sys


class TestIntegration(TestCase):

    @classmethod
    def setUpClass(cls, ):
        pass

    def setUp(self):
        pass

    def test_filename_openFile_loadsFileAndCreatesPlot(self):
        pass

    def test_plotModel_updatePlot_plotIsUpdated(self):
        pass

    def tearDown(self):
        pass