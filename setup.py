from setuptools import find_packages,setup
from typing import List
import os
import sys

#get file - requirements.txt dynamically
def file_path(file_name:str)->str:
    """
    This function will return the file path of the given file name
    """
    # get the current working directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # get the absolute path of the file
    file_path = os.path.join(current_dir, file_name)
    return file_path

requirements_txt_path = file_path('requirements.txt')
def get_requirements(file_path = file_path('requirements.txt'))->list[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name = "ML project",  
    version = "0.0.1",
    author = "Harsh kumar sharma",
    author_email = "harshsharma11d@gmail.com",
    packages = find_packages(),
    install_requires =get_requirements(requirements_txt_path),
    package_dir={'': 'src'},
    # python_requires = '>=3.10',
    # description = "A small ML project",
    # long_description = "A small ML project to learn how to create a ML project from scratch",
    # long_description_content_type = "text/markdown",
    # entry_points = {
    #     'console_scripts': [
    #         'ml_project = ml_project.__main__:main'
    #     ]
    
    # },
    # classifiers = [
    #     'Programming Language :: Python :: 3.10',
    #     'License :: OSI Approved :: MIT License',
    #     'Operating System :: OS Independent',
    # ],
    # url = ""
    # keywords = "ML, project, python, setup.py",
    # license = "MIT",
    # include_package_data = True,
    # zip_safe = False,
    # test_suite = 'tests',
    # tests_require = [
    #     'pytest',
    #     'pytest-cov',
    #     'pytest-html',
    #     'pytest-xdist',
    #     'pytest-mock',
    #     'pytest-bdd',
    #     'pytest-flake8',
    #     'pytest-pylint',
    #     'pytest-mypy',
    #     'pytest-black',
    #     'pytest-isort',
    # ],
    # extras_require = {
    #     'dev': [
    #         'black',
    #         'flake8',
    #         'mypy',
    #         'isort',
    #         'pylint',
    #         'pytest',
    #         'pytest-cov',
    #         'pytest-html',
    #         'pytest-xdist',
    #         'pytest-mock',
    #         'pytest-bdd',
    #         'pytest-flake8',
    #         'pytest-pylint',
    #         'pytest-mypy',
    #         'pytest-black',
    #         'pytest-isort',
    #     ],
    # },
    
)