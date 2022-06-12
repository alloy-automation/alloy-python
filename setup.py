import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alloy-python",
    version="0.0.1",
    description="Run Alloy workflows from a python server",
    long_description=long_description,
    py_modules=["alloy-python"],
    package_dir={'':'src'}
)