#!/usr/bin/env python
from os import path
from setuptools import setup, find_packages


pkg_name = "intanrhsreader"
here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), "r") as f:
    long_description = f.read()

with open(path.join(here, "requirements.txt")) as f:
    requirements = f.read().splitlines()

with open(path.join(here, "version.py")) as f:
    exec(f.read())

setup(
    name=pkg_name.replace("_", "-"),
    version=__version__,
    description="Intan single rhs file data reader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="DataJoint",
    author_email="info@datajoint.com",
    license="GPLv3.0",
    url=f'https://github.com/datajoint/{pkg_name.replace("_", "-")}',
    keywords="neuroscience science datajoint intan rhs reader",
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    scripts=[],
    install_requires=requirements,
)
