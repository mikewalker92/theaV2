import iris.quickplot as quickplot
from matplotlib import pyplot


def plot(cube, plot_options):
    """
    :type cube: iris.cube.Cube
    :type plot_options: thea.lib.models.plot_options_model.PlotOptions
    :rtype: Any
    """
    clear_figure()
    return quickplot.pcolormesh(cube)


def clear_figure():
    pyplot.clf()