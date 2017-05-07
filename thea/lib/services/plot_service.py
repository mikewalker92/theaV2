import iris.quickplot as quickplot
from matplotlib import pyplot

def plot_new_figure(plotted_slice, plot_selection_model):
    """
    :type plotted_slice: iris.cube.Cube
    :type plot_selection_model: thea.lib.models.plot_selection_model.PlotSelectionModel
    :rtype: pyplot.Figure
    """
    # TODO allow different plots
    figure = pyplot.figure()
    quickplot.pcolormesh(plotted_slice, figure=figure)
    return figure


def clear_figure():
    pyplot.clf()