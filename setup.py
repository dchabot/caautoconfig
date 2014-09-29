#!/usr/bin/env python

from distutils.core import setup

setup(name='CAAutoConfig',
      version='1.1',
      description='Python Utilities to autogenerate archiver file',
      author='Stuart Wilkins',
      author_email='swilkins@bnl.gov',
      url='https://github.com/NSLS-II-CSX/CAAutoConfig.git',
      license='LICENSE',
      packages=['CAAutoConfig'],
      scripts=['make-engine-cfg']
     )
