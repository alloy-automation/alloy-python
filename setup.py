# setup.py
from setuptools import setup, find_packages

setup(
    name='alloy_python',
    version='0.1.0',
    author='Your Name',
    author_email='kelly@runalloy.com',
    description='A lightweight Python wrapper for the Alloy API',
    packages=find_packages(),
    install_requires=[
        'requests',  # and any other dependencies
    ],
    # Include additional metadata as needed
)
