import os

def get_file_dict(directory):
    """
    Recursively creates a dictionary of lists of files for the given directory and its subdirectories.
    """
    file_dict = {}

    # Iterate over the contents of the current directory
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        # If it's a directory, recursively call get_file_dict on the subdirectory
        if os.path.isdir(path):
            file_dict[name] = get_file_dict(path)
        # If it's a file, add it to the file list for the current directory
        elif os.path.isfile(path):
            # If the directory isn't in the file_dict yet, add an empty list
            if directory not in file_dict:
                file_dict[directory] = []
            # Add the file to the list for the current directory
            file_dict[directory].append(name)

    return file_dict

print(get_file_dict("../borrame"))
