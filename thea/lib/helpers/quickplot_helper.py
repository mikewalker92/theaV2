import iris.quickplot as quickplot


class QuickplotHelper(object):
    """
    Convenience class which wraps the Iris Quickplot module.
    """

    def __int__(self):
        pass

    @staticmethod
    def plot_1d(cube):
        return quickplot.plot(cube)

    @staticmethod
    def pcolormesh(cube):
        return quickplot.pcolormesh(cube)

    @staticmethod
    def contour(cube):
        return quickplot.contour(cube)

    @staticmethod
    def filled_contour(cube):
        return quickplot.contourf(cube)
