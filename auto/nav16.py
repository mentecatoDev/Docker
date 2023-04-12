import os
import yaml

def clean_key(string):
    name, ext = os.path.splitext(string)
    if ext == ".md":
        string = name
    string = string.replace("_", " ")
    string = ''.join([i for i in string if not i.isdigit()])
    return string.strip()

def generate_nav_dict(path, ignore=[]):
    nav_dict = {}
    entries = sorted(os.scandir(path), key=lambda x:x.name)

    for entry in entries:
        key = clean_key(entry.name)
        if entry.is_file() and entry.name != "index.md":
            nav_dict[key] = os.path.join(path, entry.name)
        elif entry.is_dir() and entry.name not in ignore:
            subdir_nav = generate_nav_dict(entry.path)
            if subdir_nav:
                nav_dict[key] = subdir_nav

    return nav_dict

def create_mkdocs_nav_yaml(nav_dict, output_file):
    with open(output_file, "w") as outfile:
        yaml.dump(nav_dict, outfile, default_flow_style=False, default_style="", indent=2, allow_unicode=True, encoding="utf-8", sort_keys=False)


if __name__ == "__main__":
    docs_path = "../docs"
    nav_file_path = "./nav.yml"
    ignore = ["javascripts"]
    nav_dict = generate_nav_dict(docs_path, ignore=ignore)
    create_mkdocs_nav_yaml(nav_dict, nav_file_path)


    mkdocs_file_path = "../mkdocs.yml"
    output_file_path = "../mkdocs_new.yml"

    with open(nav_file_path, "r") as nav_file, \
         open(mkdocs_file_path, "r") as mkdocs_file, \
         open(output_file_path, "w") as output_file:

        for line in mkdocs_file:
            if line.strip() == "nav:":
               output_file.write("nav:\n")
               break 
            output_file.write(line)
        else:
            print("Error: la sección 'nav:' no se encuentra en el archivo mkdocs.yml")
            exit(1)
        for line in nav_file:
            output_file.write("  " + line)
        output_file.write("\n")
        copia = False
        for line in mkdocs_file:
            if not copia and line.strip() != "":
                continue
            else:
                for line in mkdocs_file:           
                    output_file.write(line)

    os.rename(mkdocs_file_path, mkdocs_file_path + ".bak")
    os.rename(output_file_path, mkdocs_file_path)
