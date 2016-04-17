from thea.lib.models.information_model import InformationModel
from thea.lib.models.options_model import OptionsModel
from thea.lib.models.plot_model import PlotModel


class ModelProvider(object):
    def __init__(self):
        self._informationModel = InformationModel()
        self._plot_model = PlotModel()
        self._options_model = OptionsModel()

    @property
    def information_model(self):
        """
        :rtype: InformationModel
        """
        return self._informationModel

    @property
    def plot_model(self):
        """
        :rtype: PlotModel
        """
        return self._plot_model

    @property
    def options_model(self):
        """
        :rtype: OptionsModel
        """
        return self._options_model

_model_provider = ModelProvider()


def get_model_provider():
    """
    :rtype: ModelProvider
    """
    return _model_provider