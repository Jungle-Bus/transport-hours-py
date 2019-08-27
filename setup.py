# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='transporthours',
    version='0.0.1',
    description='Package for handling public transport routes opening hours from OpenStreetMap',
    long_description=readme,
    author='Adrien Pavie',
    author_email='panieravide@riseup.net',
    url='https://github.com/JungleBus/transport-hours-py',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
