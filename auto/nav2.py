import os
import toml

docs_dir = '../borrame'
nav = []

# Walk through the '../borrame' directory and its subdirectories

for root, dirs, files in os.walk(docs_dir):
    # Ignore hidden files
    files = [f for f in files if not f[0] == '.']
    dirs[:] = [d for d in dirs if not d[0] == '.']
    
    # If we're in the root folder, add the files to the nav
    if root == docs_dir:
        section_files = [f[:-3] for f in files if f.endswith('.md')]
        nav += sorted(section_files)
    # If we're in a subfolder, add the files to a subsection
    else:
        section_name = os.path.basename(root)
        section_files = [f[:-3] for f in files if f.endswith('.md')]
        nav.append({section_name: sorted(section_files)})

# Debugging output: print the nav list
print(nav)

# Generate the navigation section as a TOML string
nav_toml = toml.dumps({'nav': nav})

# Print the generated TOML string
print(nav_toml)