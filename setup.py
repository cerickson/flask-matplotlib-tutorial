#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='flaskplotlib',
      version='0.1alpha',
      description='Python 3.6, Flask, and Matplotlib Tutorial',
      author='Chris Erickson',
      author_email='erickson.christopher.k@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      requires=['flask', 'numpy', 'matplotlib']
     )
