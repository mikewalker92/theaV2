from thea.lib.models.base_model import BaseModel


class PlotModel(BaseModel):
    """
    Model containing the matplotlib plot object to display.
    """

    def __init__(self):
        super(BaseModel, self).__init__()

        self._current_plot = None

    def set_current_plot(self, current_plot):
        self._current_plot = current_plot
        self.announce_update()

    def get_current_plot(self):
        return self._current_plot