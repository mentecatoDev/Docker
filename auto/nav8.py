import os
import yaml

def create_docs_structure(path):
    """
    Recibe una ruta path y devuelve un diccionario con la estructura del directorio
    """
    result = {}
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path):
            result[item] = None
        elif os.path.isdir(full_path):
            sub_items = create_docs_structure(full_path)
            if sub_items:
                result[item] = sub_items
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
            nav_list.append({item: create_mkdocs_nav(sub_items)})
    return yaml.dump(nav_list)


docs_path = '../borrame'
nav_content = create_mkdocs_nav(docs_path)
with open("yamel.yml", "w") as f:
    f.write(f"nav:\n{nav_content}")