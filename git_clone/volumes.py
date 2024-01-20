def add_volume(output_volume, operator):
    operator.add_volume(output_volume)
    pvolumes = {str(output_volume.name): output_volume}
    operator.add_pvolumes(pvolumes)

    return operator
