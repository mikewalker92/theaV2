class MainController(object):
    def __init__(self, main_service):
        self.main_service = main_service

    def open_file(self, filename):
        self.main_service.open_file()