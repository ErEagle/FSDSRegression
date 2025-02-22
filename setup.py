from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT= '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_opj:
        requirements=file_opj.readlines()
        [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements





setup(
    name='RegressorProject',
    version='0.0.1',
    author='Vines',
    author_email='vines04460@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()

)
