import os

licence_names = ['Apache-2.0']
LICENSES = {}
dir_path = os.path.dirname(os.path.abspath(__file__))
for i in licence_names:
    with open(f'{dir_path}/{i}.txt', 'r') as file:
        LICENSES[i] = file.read()

del dir_path, licence_names, i, file

__all__ = ['LICENSES']
