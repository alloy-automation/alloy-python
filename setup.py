# setup.py
from setuptools import setup, find_packages

setup(
    name='alloy_python_sdk',
    version='0.1.0',
    author='Kelly Gold',
    author_email='kelly@runalloy.com',
    description='A lightweight Python wrapper for the Alloy API',
    long_description=open('README.md').read(),  # Ensure you have a README.md file
    long_description_content_type='text/markdown',
    url='https://github.com/alloy-automation/alloy-python',  # Replace with your repository URL
    packages=find_packages(),
    install_requires=[
        'requests',  # Add other dependencies as needed
    ],
    classifiers=[
        # Classifiers help users find your project
        # Full list: https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Update if you have a different license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
)
