from thea.lib.models.view_model import get_view_model, ViewModel
from thea.lib.services.cube_collapsing_service import get_plotted_slice, get_selected_cube
from thea.lib.services.plot_service import plot_new_figure
from thea.lib.services.populate_cube_details_service import populate_cube_details_model


class UpdatePlotController(object):

    def __init__(self, view_model):
        """
        :type view_model: ViewModel
        """
        self.__cube_details_model = view_model.cube_details
        self.__plot_model = view_model.plot
        self.__user_selection_model = view_model.user_selection
        self.__plot_selection_model = view_model.user_selection.plot_selection

    def update_plot(self):
        # TODO should this live in the NewCubeController Class?
        selected_cube = get_selected_cube(self.__user_selection_model)
        plotted_slice = get_plotted_slice(self.__user_selection_model)

        populate_cube_details_model(self.__cube_details_model, selected_cube, plotted_slice)

        figure = plot_new_figure(plotted_slice, self.__plot_selection_model)
        self.__plot_model.figure.value = figure


_update_plot_controller = UpdatePlotController(get_view_model())


def get_update_plot_controller():
    """
    :rtype: UpdatePlotController
    """
    return _update_plot_controller