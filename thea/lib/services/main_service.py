class MainService(object):
    def __init__(self, plot_service):
        self.plot_service = plot_service

    def open_file(self):
        self.plot_service.plot_cube()