import os
import yaml

def clean_key(string):
    if string[-3:] == ".md":
        string = string[:-3]
    string = string.replace("_", " ")
    string = ''.join([i for i in string if not i.isdigit()])
    return string.strip()

def generate_nav_dict(path):
    nav_dict = {}
    entries = sorted(os.scandir(path), key=lambda x:x.name)
    print ("Gigante : ", entries)
    for entry in entries:
        key = clean_key(entry.name)
        if entry.is_file() and entry.name != "index.md":
            nav_dict[key] = os.path.join(path, entry.name)
        elif entry.is_dir():
            subdir_nav = generate_nav_dict(entry.path)
            if subdir_nav:
                nav_dict[key] = subdir_nav

    return nav_dict

def create_mkdocs_nav_yaml(nav_dict, output_file):
    with open(output_file, "w") as outfile:
        outfile.write("nav:\n")
        print ("Gigante : ", nav_dict)
        yaml.dump(nav_dict, outfile, default_flow_style=False, default_style="", indent=2, allow_unicode=True, encoding="utf-8", sort_keys=False)

if __name__ == "__main__":
    docs_path = "../borrame"
    output_file = "nav.yml"

    nav_dict = generate_nav_dict(docs_path)
    create_mkdocs_nav_yaml(nav_dict, output_file)