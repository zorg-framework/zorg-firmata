#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

try:
    from pypandoc import convert
    readme = lambda f: convert(f, "rst")
except ImportError:
    print("Module pypandoc not found, could not convert Markdown to RST")
    readme = lambda f: open(f, "r").read()

req = open("requirements.txt")
requirements = req.readlines()
req.close()

setup(
    name="zorg-firmata",
    version="0.0.2",
    url="https://github.com/zorg/zorg-firmata",
    description="Firmata adapter for the Zorg framework.",
    long_description=readme("README.md"),
    author="Zorg Group",
    author_email="gunthercx@gmail.com",
    packages=find_packages(),
    package_dir={"zorg_firmata": "zorg_firmata"},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=True,
    platforms=["any"],
    keywords=["zorg", "firmata"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    test_suite="tests",
    tests_require=[]
)
