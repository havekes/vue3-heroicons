import os
import requests
import zipfile
import shutil
import typing

HEROICONS_ZIP_URL = 'https://github.com/tailwindlabs/heroicons/archive/master.zip'
ZIP_NAME = 'heroicons-master.zip'
DIR_NAME = 'heroicons-master'
ROOT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')
COMPONENTS_PATH = os.path.join(ROOT_PATH, 'components/Icons')


def download_and_extract():
    """ Download heroicon from repository into ROOT_PATH and extract"""
    os.makedirs(ROOT_PATH, exist_ok=True)

    # Download heroicons master zip
    r = requests.get(HEROICONS_ZIP_URL)
    with open(os.path.join(ROOT_PATH, ZIP_NAME), 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)

    # Extract
    zipfile.ZipFile(os.path.join(ROOT_PATH, ZIP_NAME)).extractall(ROOT_PATH)


def cleanup(remove_lib):
    """
    Remove downloaded and generated files

    Params:
        remove_lib - True will also remove generated components and index.ts files
    """
    try:
        os.remove(os.path.join(ROOT_PATH, ZIP_NAME))
        if remove_lib:
            os.remove(os.path.join(ROOT_PATH, 'index.ts'))
    except OSError:
        pass
    shutil.rmtree(os.path.join(ROOT_PATH, DIR_NAME), ignore_errors=True)
    if remove_lib:
        shutil.rmtree(os.path.join(COMPONENTS_PATH,
                                   "Outline"), ignore_errors=True)
        shutil.rmtree(os.path.join(COMPONENTS_PATH,
                                   "Solid"), ignore_errors=True)


def create_vue_component(entry: os.DirEntry, directory_name: str, prefix: str) -> str:
    """
    Generate a Vue component file from an svg file

    Params:
        entry - SVG file
        directory_name - Outline or Solid directory
        prefix - cmponent prefix (O or S)

    Return:
        Export line for index.ts
    """
    os.makedirs(os.path.join(COMPONENTS_PATH, directory_name), exist_ok=True)

    with open(entry.path, 'r') as file:
        lines = file.readlines()
        icon = '\n'
        for line in lines:
            icon += '  ' + line

    component_name = entry.name
    component_name = component_name[:0] + \
        component_name[0].upper() + component_name[0 + 1:]

    # Kebab case to camel case
    for c in component_name:
        if c == '-':
            dash_index = component_name.index(c)
            component_name = component_name[:dash_index] + \
                component_name[dash_index + 1:]
            component_name = component_name[:dash_index] + \
                component_name[dash_index].upper() + \
                component_name[dash_index + 1:]

    component_name = os.path.splitext(prefix + component_name)[0]

    component_path = os.path.join(
        COMPONENTS_PATH, directory_name, component_name + '.vue')

    with open(component_path, 'w') as f:
        f.write(f"""<template>{icon}</template>

<script lang="ts">
import {{ defineComponent }} from 'vue'
export default defineComponent({{
  name: '{component_name}'
}})
</script>""")

    return f'export {{ default as {component_name} }} from \'./components/Icons/{directory_name}/{component_name}.vue\'\n'


cleanup(True)
download_and_extract()

index_ts = ''
with os.scandir(os.path.join(ROOT_PATH, DIR_NAME, 'optimized/outline')) as directories:
    for entry in directories:
        index_ts += create_vue_component(entry, 'Outline', 'O')

with os.scandir(os.path.join(ROOT_PATH, DIR_NAME, 'optimized/solid')) as directories:
    for entry in directories:
        index_ts += create_vue_component(entry, 'Solid', 'S')

with open(os.path.join(ROOT_PATH, 'index.ts'), 'w') as f:
    f.write(index_ts)

cleanup(False)
