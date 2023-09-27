from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = "-e . "
def get_requirements(file_path:str) -> List[str]:
    '''
    This function return list of requirements
    '''
    with open(file=file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [requirement.replace("\n","") for requirement in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements

setup(
    name="restaurant_rating_prediction",
    version="0.0.1",
    author="Krish",
    author_email="krishkanojia7@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)