class Properties(object):
    def __init__(self):
        self._render_ui = True

    @property
    def render_ui(self):
        return self._render_ui

    @render_ui.setter
    def render_ui(self, render_ui):
        self._render_ui = render_ui


_properties = Properties()


def properties():
    return _properties