from thea.lib.models.base_model import BaseModel


class PlotModel(BaseModel):
    """
    Model containing the matplotlib plot object to display.
    """

    def __init__(self):
        super(PlotModel, self).__init__()
        self._current_plot = None

    @property
    def current_plot(self):
        return self._current_plot

    @current_plot.setter
    def current_plot(self, value):
        self._current_plot = value
        self.announce_update()


_plot_model = PlotModel()


def get_plot_model():
    return _plot_model