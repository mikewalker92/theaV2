import iris.quickplot as quickplot
from matplotlib import pyplot


def plot_new_figure(plotted_slice, plot_selection_model):
    """
    :type plotted_slice: iris.cube.Cube
    :type plot_selection_model: thea.lib.models.plot_selection_model.PlotSelectionModel
    """
    clear_figure()
    # TODO allow different plots
    return quickplot.pcolormesh(plotted_slice)


def clear_figure():
    pyplot.clf()