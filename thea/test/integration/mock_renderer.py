class MockRenderer(object):
    """
    A mock renderer which will not actually draw the view.
    """

    def __init__(self):
        self._shown_views = []
        self._shown_maximized = []

    @property
    def shown_views(self):
        return self._shown_views

    @property
    def shown_maximized(self):
        return self._shown_maximized

    def show(self, view):
        self._shown_views.append(view)

    def show_maximized(self, window):
        self._shown_maximized.append(window)

    def reset(self):
        self._shown_views = []
        self._shown_maximized = []