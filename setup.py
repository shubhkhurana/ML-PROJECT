from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]: ##will return list which contains str
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
    return requirements





setup(
name='ML-Project',
version="0.0.1",
author="SK",
author_email="shubh.khurana06@gmail.com",
packages=find_packages(), # will find packages automatically  
install_requires=get_requirements('requirements.txt')

)