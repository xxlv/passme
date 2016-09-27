# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='passme',
    version='1.0.0',
    description='Passme! check your password',
    long_description=readme,
    author='ghost',
    author_email='lvxiang119@gmail.com',
    url='https://github.com/xxlv/passme',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
