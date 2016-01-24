import iris


def load_file(filename, options_model):
    options_model.add_cubes(iris.load_cubes(filename))