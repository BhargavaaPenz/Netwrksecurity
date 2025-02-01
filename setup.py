''' 
The setup.py file for the package
'''

from setuptools import setup,find_packages
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt') as f:
            #reading the requirements.txt file
            lines = f.readlines()
            for line in lines:
                requirements=line.strip()
                ##ignore the empty lines
                if requirements and requirements != '-e .':
                    requirement_list.append(requirements)

    except FileNotFoundError:
        print('File not found')
    return requirement_list

setup(
    name='Networksec',
    version='0.0.1',
    description='A package for building a ML project',
    author='Bhargavaa',
    author_email="g.bhargavaa@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)