#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

setup(
        name = "csv2xlsx",
        version = "0.1",
        author = "Dillon Barker",
        author_email = "dorbarker@github.com",
        description = "Wraps CSV files as worksheets in a MS Excel workbook",
        license = "BSD",
        url = "https://github.com/dorbarker/csv2xlsx",
        keywords = "csv xlsx excel",
        install_requires = ["xlsxwriter"],
        py_modules = ['csv2xlsx'],
        entry_points =  {
            'console_scripts': [
                'csv2xlsx=csv2xlsx:main'
                ]
            },
        classifiers = [
            "Development Status :: 3 - Alpha",
            "Topic :: Utilities",
            "License :: OSI Approved :: BSD License",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.0",
            "Programming Language :: Python :: 3.1",
            "Programming Language :: Python :: 3.2",
            "Programming Language :: Python :: 3.4"
            ]

)
