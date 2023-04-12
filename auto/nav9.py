# -*- coding: utf-8 -*-


import os
import yaml

def create_docs_structure(path):
    """
    Recibe una ruta path y devuelve un diccionario con la estructura del directorio
    """
    result = {}
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                result[entry.name] = None
            elif entry.is_dir():
                sub_items = create_docs_structure(entry.path)
                if sub_items:
                    result[entry.name] = sub_items
    return result

def create_mkdocs_nav(docs_path):
    """
    Recibe una ruta docs_path y devuelve un string con el contenido yaml de la sección nav de mkdocs
    """
    docs_structure = create_docs_structure(docs_path)
    nav_list = []
    for item, sub_items in docs_structure.items():
        if sub_items is None:
            nav_list.append(item)
        else:
            sub_path = os.path.join(docs_path, item)
            nav_list.append({item: create_mkdocs_nav(sub_path)})
    print('Gigante: ', nav_list)
    return yaml.dump(nav_list, allow_unicode=True, encoding="utf-8")


docs_path = '../borrame'
nav_content = create_mkdocs_nav(docs_path)
with open("yamel.yml", "w") as f:
    f.write(f"nav:\n{nav_content}")