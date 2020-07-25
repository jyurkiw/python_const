import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_const",
    version="1.0",
    description="A small utility for creating constants containers.",
    url="https://github.com/jyurkiw/python_const",
    author="Jeffrey Yurkiw",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Pythong :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
)
