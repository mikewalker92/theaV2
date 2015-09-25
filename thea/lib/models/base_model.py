class BaseModel(object):
    def __init__(self):
        self.__update_functions = []

    def subscribe_update_function(self, function):
        if function not in self.__update_functions:
            self.__update_functions.append(function)

    def announce_update(self):
        for function in self.__update_functions:
            function()