from thea.lib.views.thea_widget import TheaWidget


class PlotOptionsWidget(TheaWidget):
    def __init(self):
        super(PlotOptionsWidget, self).__init__()


_plot_options_widget = PlotOptionsWidget()


def get_plot_options_widget():
    return _plot_options_widget