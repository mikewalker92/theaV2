import iris.quickplot as quickplot
from matplotlib import pyplot


def plot(cube, plot_options):
    clear_figure()
    return quickplot.pcolormesh(cube)


def clear_figure():
    pyplot.clf()