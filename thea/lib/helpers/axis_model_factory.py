from thea.lib.models.axis_model import AxisModel


def create_axis_model(dimension_coord):
    """
    :type dimension_coord: iris.coords.DimCoord
    :rtype: AxisModel
    """
    return AxisModel(
        name=dimension_coord.name()
    )
