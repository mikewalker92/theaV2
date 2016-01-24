from thea.lib.models.base_model import BaseModel


class PlotModel(BaseModel):
    def __init__(self):
        super(PlotModel, self).__init__()

        self._current_plot = None

    @property
    def current_plot(self):
        return self._current_plot

    @current_plot.setter
    def current_plot(self, plot):
        self._current_plot = plot
        self.announce_update()

    def clear(self):
        self._current_plot = None