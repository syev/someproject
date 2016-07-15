#!/usr/bin/env python

from setuptools import setup

setup(name="someproject",
      version="1.0.0",
      description="Testing project stuff",
      url="https://www.github.com/syev/someproject",
      install_requires=["dependency"],
      packages=["someproject"],
      scripts=[],
      test_suite="test",
      dependency_links=[
          "git+ssh://git@github.com/syev/dependency.git#egg=dependency-1.0.0",
          ])
