import setuptools
import os

DIRECTORY = os.path.dirname(__file__)
READ_ME = open(os.path.join(DIRECTORY, "README.rst")).read()

setuptools.setup(
    name="alloy-python",
    version="0.0.1",
    description="Run Alloy workflows from a python server",
    long_description=READ_ME,
    long_description_content_type="text/x-rst",
    py_modules=["alloy-python"],
    package_dir={'':'src'}
)