from setuptools import setup
from setuptools import find_packages

setup(
    name='mypackage',
    version='0.0.1',
    install_requires=[
        'requests',
        'importlib-metadata; python_version == "3.8"',
    ],
    packages=find_packages(
        # All keyword arguments below are optional:
        where='mypackage',  # '.' by default
        include=['mypackage*'],  # ['*'] by default
        exclude=['mypackage.tests'],  # empty by default
    ),
)
