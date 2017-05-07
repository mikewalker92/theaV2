
def get_selected_cube(user_selection_model):
    """
    :type user_selection_model: thea.lib.models.user_selection_model.UserSelectionModel
    :rtype: iris.cube.Cube
    """
    return user_selection_model.cube_selection.cubes.selected_item


def get_plotted_slice(user_selection_model):
    """
    :type user_selection_model: thea.lib.models.user_selection_model.UserSelectionModel
    :rtype: iris.cube.Cube
    """
    # TODO implement this.
    return get_selected_cube(user_selection_model)