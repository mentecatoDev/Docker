import os

docs_dir = "../borrame"  # Directorio de documentos
nav = []  # Lista de secciones y subsecciones
ignore = ["javascripts"] # Lista de directorios que hay que ignorar

# Recorremos la estructura de archivos en el directorio de documentos

for root, dirs, files in os.walk(docs_dir):
    print("Gigante:", root, dirs, files)
    if root == docs_dir:
        # Si estamos en el directorio principal, añadimos las secciones
        for dir in sorted(dirs):
            print("Gigante", dir)
            if not dir in ignore:
                nav.append(dir)
    else:
        # Si estamos en un subdirectorio, añadimos las subsecciones
        subnav = []
        for file in sorted(files):
            if file.endswith(".md"):
                # Solo añadimos archivos Markdown a la navegación
                subnav.append(os.path.splitext(file)[0])
        if subnav:
            # Si hay subsecciones, añadimos la sección con las subsecciones ordenadas
            nav.append({os.path.basename(root): subnav})

# Imprimimos la sección de navegación en formato YAML
print("nav:")
print("  - Home: index")
for item in nav:
    if isinstance(item, str):
        print(f"  - {item}: {item}/index")
    else:
        for section, subnav in item.items():
            print(f"  - {section}:")
            for subitem in subnav:
                print(f"    - {subitem}: {section}/{subitem}")
print(nav)
