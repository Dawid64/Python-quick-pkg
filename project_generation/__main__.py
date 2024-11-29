from collections import defaultdict
from dataclasses import dataclass
import pprint
from typing import Dict, List, Optional, Union
from project_generation import LICENSES
import os

INIT = '__init__.py'

@dataclass
class PackageTreeClass:
    name:str
    parent:Optional["PackageTreeClass"] = None
    children:List[Union["PackageTreeClass",str]] = None

def get_code_structure(package_name):
    package_tree = PackageTreeClass(name=package_name)
    tree: Dict[str, PackageTreeClass] = defaultdict(lambda: None)
    tree[package_name] = package_tree
    for root, dirs, files in os.walk(package_name):
        name = os.path.basename(root)
        tree[name] = PackageTreeClass(name=name)
        parent = os.path.basename(os.path.dirname(root))
        tree[name].parent = tree[parent]
        for file in sorted(files):
            if tree[name].children is None:
                tree[name].children = []
            tree[name].children.append(file)
        for dir in sorted(dirs):
            if tree[name].children is None:
                tree[name].children = []
            tree[name].children.append(tree[dir])
    pprint.pprint(tree)
        
    

def create_project():

    selected_license = 'Apache-2.0'
    with open('LICENSE', 'w') as file:
        file.write(LICENSES[selected_license])
    
if __name__ == '__main__':
    # create_project()
    get_code_structure('sample_project')