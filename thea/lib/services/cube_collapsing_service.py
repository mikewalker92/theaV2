
def get_selected_cube(user_selection_model):
    return user_selection_model.cube_selection.cubes.selected_item


def get_plotted_slice(user_selection_model):
    # TODO implement this.
    return get_selected_cube(user_selection_model)
