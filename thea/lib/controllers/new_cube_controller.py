from thea.lib.models.view_model import get_view_model
from thea.lib.services.cube_collapsing_service import get_selected_cube, get_plotted_slice
from thea.lib.services.load_file_service import load_cubes_from_file
from thea.lib.services.populate_cube_details_service import populate_cube_details_model
from thea.lib.services.populate_user_selection_service import populate_user_selection_model, set_cubes_in_file
from thea.lib.services.plot_service import plot_new_figure


class NewCubeController(object):
    def __init__(self, view_model):
        """
        :type view_model: thea.lib.models.view_model.ViewModel
        """
        self.__cube_details_model = view_model.cube_details
        self.__plot_model = view_model.plot
        self.__user_selection_model = view_model.user_selection
        self.__plot_selection_model = view_model.user_selection.plot_selection

    def open_file(self, filename):
        """
        :type filename: str
        """
        cubes = load_cubes_from_file(filename)

        set_cubes_in_file(self.__user_selection_model, cubes)

        self.__load_current_cube()

    def switch_cube(self):
        self.__load_current_cube()

    def __load_current_cube(self):
        self.__user_selection_model = populate_user_selection_model(self.__user_selection_model)

        selected_cube = get_selected_cube(self.__user_selection_model)
        plotted_slice = get_plotted_slice(self.__user_selection_model)

        populate_cube_details_model(self.__cube_details_model, selected_cube, plotted_slice)

        figure = plot_new_figure(plotted_slice, self.__plot_selection_model)
        self.__plot_model.figure.value = figure

__new_cube_controller = NewCubeController(get_view_model())


def get_new_cube_controller():
    """
    :rtype: NewCubeController
    """
    return __new_cube_controller