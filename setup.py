"""Python setup.py for sprint2 package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("sprint2", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="sprint2",
    version=read("sprint2", "VERSION"),
    description="Awesome sprint2 created by Josenino04",
    url="https://github.com/Josenino04/Sprint2/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Josenino04",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["sprint2 = sprint2.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
