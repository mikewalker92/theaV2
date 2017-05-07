from thea.lib.models.cube_details_model import CubeDetailsModel
from iris.cube import Cube


def populate_cube_details_model(cube_details_model, selected_cube, plotted_slice):
    """
    :type cube_details_model: CubeDetailsModel
    :type selected_cube: Cube
    :type plotted_slice: Cube
    """
    cube_details_model.cube_readout.value = str(selected_cube)
    cube_details_model.slice_readout.value = str(plotted_slice)