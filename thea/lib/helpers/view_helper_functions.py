from PySide.QtGui import QComboBox


def get_axis_name(axis):
    # TODO fill this in.
    return 'axis name'


def get_cube_name(cube):
    # TODO implement this properly
    return 'cube name'


def get_all_item_names(combo_box):
    """
    :type combo_box: QComboBox
    :rtype: list[str]
    """
    return [combo_box.itemText(i) for i in xrange(combo_box.count())]