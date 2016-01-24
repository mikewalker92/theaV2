from thea.lib.services.cube_collapsing_service import collapse
from thea.lib.services.plotting_service import plot


def update_plot(plot_model, options_model):
    cube_to_plot = collapse(options_model.current_cube, options_model.axes_model)
    plot_model.current_plot = plot(cube_to_plot, options_model.plot_options)