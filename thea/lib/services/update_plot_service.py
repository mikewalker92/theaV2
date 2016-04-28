from thea.lib.services.cube_collapsing_service import collapse
from thea.lib.services.plotting_service import plot


def update_plot(view_model):
    """
    :type view_model: thea.lib.models.view_model.ViewModel
    """
    cube_to_plot = collapse(view_model.cube)
    view_model.plot.current_plot = plot(cube_to_plot, view_model.options.plot_options)