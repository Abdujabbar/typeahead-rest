def get_contents(path):

    with open(path, "r") as context:
        for line in context:
            yield line
