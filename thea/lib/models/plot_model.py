from thea.bound.source import BoundValue
from thea.lib.models.base_model import BaseModel
import matplotlib.pyplot as plt


class PlotModel(BaseModel):
    def __init__(self):
        super(PlotModel, self).__init__()
        self.__current_plot = BoundValue(get_current_figure())

    def clear(self):
        clear_figure()
        self.__current_plot.value = get_current_figure()

    @property
    def current_plot(self):
        return self.__current_plot


def get_current_figure():
    return plt.gcf()


def clear_figure():
    plt.clf()