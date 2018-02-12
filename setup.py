#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name="GIClient",
      version="0.1",
      description="Small api client to help with interacting with Ghost Inspector",
      author="Cameron Stiles",
      author_email="cstiles187@gmail.com",
      url="",
      install_requires=['pytest>=2.8.1', 'requests>=2.7', 'pyyaml'],
      packages = find_packages(),
      license = "MIT License",
      keywords="GhostInspector",
      zip_safe = True)
