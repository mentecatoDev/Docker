import os
import yaml

def clean_key(string):
    """
    Formats a given string by removing digits, underscores, and the ".md" extension if present.

    Parameters:
    string (str): The string to be formatted.

    Returns:
    str: The formatted string.
    """
    if string[-3:] == ".md":
        string = string[:-3]  # Removes ".md" extension if present
    string = string.replace("_", " ")  # Replaces underscores with spaces
    string = ''.join([i for i in string if not i.isdigit()])  # Removes digits
    return string.strip()

def generate_nav_dict(path):
    """
    Recursively generates a navigation dictionary from the file and directory structure at the given path.

    Parameters:
    path (str): The path to the directory to be navigated.

    Returns:
    dict: The navigation dictionary.
    """
    nav_dict = {}
    entries = sorted(os.scandir(path), key=lambda x:x.name)  # Gets directory entries sorted by name

    for entry in entries:
        key = clean_key(entry.name)
        if entry.is_file() and entry.name != "index.md":
            # If the entry is a file and not the index file, add it to the dictionary with its path
            nav_dict[key] = os.path.join(path, entry.name)
        elif entry.is_dir():
            # If the entry is a directory, generate a sub-navigation dictionary recursively
            subdir_nav = generate_nav_dict(entry.path)
            if subdir_nav:
                nav_dict[key] = subdir_nav  # Add the sub-navigation dictionary to the parent dictionary

    return nav_dict

def create_mkdocs_nav_yaml(nav_dict, output_file):
    """
    Writes the given navigation dictionary to a YAML file with the given output file name.

    Parameters:
    nav_dict (dict): The navigation dictionary to be written to the file.
    output_file (str): The name of the output file.
    """
    with open(output_file, "w") as outfile:
        outfile.write("nav:\n")  # Writes the "nav:" key to the beginning of the file
        # Writes the navigation dictionary to the file as YAML with specified formatting options
        yaml.dump(nav_dict, outfile, default_flow_style=False, default_style="", indent=2, allow_unicode=True, encoding="utf-8", sort_keys=False)

if __name__ == "__main__":
    docs_path = "../borrame"  # Path to directory containing files to be navigated
    output_file = "./nav.yml"  # Name of output navigation file

    nav_dict = generate_nav_dict(docs_path)  # Generates the navigation dictionary
    create_mkdocs_nav_yaml(nav_dict, output_file)  # Writes the navigation dictionary to the output file as YAML
    nav_file_path = "./nav.yml"
    mkdocs_file_path = "../mkdocs.yml"
    output_file_path = "../mkdocs_new.yml"

    with open(nav_file_path, "r") as nav_file, \
         open(mkdocs_file_path, "r") as mkdocs_file, \
         open(output_file_path, "w") as output_file:

        # Copiar el contenido del archivo mkdocs.yml hasta la sección 'nav:'
        for line in mkdocs_file:
            output_file.write(line)
            if line.strip() == "nav:":
                break
        else:
            # Si la sección 'nav:' no se encuentra en el archivo mkdocs.yml,
            # lanzar un mensaje de error y salir del programa
            print("Error: la sección 'nav:' no se encuentra en el archivo mkdocs.yml")
            exit(1)

        # Leer y escribir el contenido del archivo nav.yml
        for line in nav_file:
            output_file.write(line)

        # Copiar el resto del contenido del archivo mkdocs.yml después de la sección 'nav:'
        copy = False
        for line in mkdocs_file:
            if line.strip() == "nav:":
                copy = True
            if copy:
                output_file.write(line)

    # Renombrar los archivos
    os.rename(mkdocs_file_path, mkdocs_file_path + ".bak")
    os.rename(output_file_path, mkdocs_file_path)
