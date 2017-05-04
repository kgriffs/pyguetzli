#!/usr/bin/env python
# encoding: UTF-8

import os
import subprocess

from setuptools import setup, find_packages
from setuptools.command.build_py import build_py


class CustomBuildPy(build_py):

    def run(self):
        subprocess.call("cd guetzli/ && make", shell=True)
        build_py.run(self)


long_description = ""
if os.path.isfile("README.rst"):
    long_description = open("README.rst", "r").read()
elif os.path.isfile("README.md"):
    long_description = open("README.md", "r").read()


setup(
    name="pyguetzli",
    version="0.0.0",
    description="Python bindings for Google's Guetzli, a JPEG encoder that optimises JPEG compression",
    url="https://github.com/wanadev/pyguetzli",
    license="Apache-2.0",

    long_description=long_description,
    keywords="image jpeg optimize guetzli",

    author="Wanadev",
    author_email="contact@wanadev.fr",
    maintainer="Fabien LOISON, Alexis BREUST",

    # platforms=["Linux"],

    packages=find_packages(),

    setup_requires=["cffi>=1.0.0"],
    cffi_modules=["pyguetzli/guetzli_build.py:ffibuilder"],
    install_requires=["cffi>=1.0.0"],

    cmdclass={
        "build_py": CustomBuildPy,
    },
)

