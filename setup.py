import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alloy-sdk",
    version="0.0.1",
    description="Run Alloy workflows from a python server",
    py_modules=["alloy-sdk"],
    package_dir={'':'src'}
)