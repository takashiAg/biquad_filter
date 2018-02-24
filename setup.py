# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='biquad_filter',
    version='0.0.1',
    description='filtering as',
    long_description=readme,
    author='Ryosuke Ando',
    author_email='ryo@ando.link',
    url='https://github.com/takashiAg/biquad_filter.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)

