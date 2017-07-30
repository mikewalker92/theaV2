
def get_axis_name(axis):
    return axis.name()


def get_cube_name(cube):
    return cube.name()


def get_all_item_names(combo_box):
    return [combo_box.itemText(i) for i in range(combo_box.count())]
