
def populate_cube_details_model(cube_details_model, selected_cube, plotted_slice):
    cube_details_model.cube_readout.value = str(selected_cube)
    cube_details_model.slice_readout.value = str(plotted_slice)
    cube_details_model.slice_data.value = plotted_slice.data
