#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for climath.

    This file was generated with PyScaffold 3.0.3.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: http://pyscaffold.org/
"""

import sys
from setuptools import setup

# Add here console scripts and other entry points in ini-style format
entry_points = """
[console_scripts]
# script_name = climath.module:function
climath = climath.climath:run
climath-add = climath.binary.add:run
climath-subtract = climath.binary.subtract:run
climath-multiply = climath.binary.multiply:run
climath-divide = climath.binary.divide:run
"""


def setup_package():
    needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
    sphinx = ['sphinx'] if needs_sphinx else []
    setup(setup_requires=['pyscaffold>=3.0a0,<3.1a0'] + sphinx,
          entry_points=entry_points,
          use_pyscaffold=True)


if __name__ == "__main__":
    setup_package()
