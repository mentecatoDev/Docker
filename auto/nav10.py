import os
import yaml

def generate_nav_dict(path):
    nav_dict = {}
    for entry in os.scandir(path):
        if entry.is_file() and entry.name != "index.md":
            nav_dict[entry.name] = os.path.join(path, entry.name)
        elif entry.is_dir():
            subdir_nav = generate_nav_dict(entry.path)
            if subdir_nav:
                nav_dict[entry.name] = subdir_nav

    return nav_dict

def create_mkdocs_nav_yaml(nav_dict, output_file):
    with open(output_file, "w") as outfile:
        outfile.write("nav:\n")
        yaml.dump(nav_dict, outfile, default_flow_style=False, default_style="", indent=2, allow_unicode=True, encoding="utf-8")

if __name__ == "__main__":
    docs_path = "../borrame"
    output_file = "nav.yml"

    nav_dict = generate_nav_dict(docs_path)
    create_mkdocs_nav_yaml(nav_dict, output_file)
