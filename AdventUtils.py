def get_data_from_file(filename):
    print("Setup - Getting test data")
    print("Getting values from [{}]".format(filename))
    with open(filename, 'r') as f:
        depths = [line.strip() for line in f]
    print("Found [{}] lines of data\n".format(len(depths)))
    return depths
