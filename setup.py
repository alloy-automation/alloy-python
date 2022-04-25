import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alloy",
    version="0.0.1",
    description="Quicksample Test Package for SQLShack Demo",
    py_modules=["alloy"],
    package_dir={'':'src'}
)