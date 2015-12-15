from thea.lib.helpers.plotting_utils import colormesh


def update_plot(cube_selection_model, plot_model):
    cube = cube_selection_model.selected_cube()
    new_plot = colormesh(cube)
    plot_model.current_plot = new_plot