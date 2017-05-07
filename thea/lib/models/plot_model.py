from thea.bound.source import BoundValue
import matplotlib.pyplot as plt


class PlotModel():
    def __init__(self):
        self.__current_plot = BoundValue(get_current_figure())

    @property
    def figure(self):
        return self.__current_plot


def get_current_figure():
    return plt.gcf()


def clear_figure():
    plt.clf()