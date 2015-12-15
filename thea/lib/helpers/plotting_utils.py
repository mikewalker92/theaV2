import iris.quickplot as quickplot
from matplotlib import pyplot


def plot_1d(cube):
    clear_figure()
    return quickplot.plot(cube)


def colormesh(cube):
    clear_figure()
    return quickplot.pcolormesh(cube)


def contour(cube):
    clear_figure()
    return quickplot.contour(cube)


def filled_contour(cube):
    clear_figure()
    return quickplot.contourf(cube)


def clear_figure():
    pyplot.clf()