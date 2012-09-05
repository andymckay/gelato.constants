import os

from setuptools import setup, find_packages


setup(name='gelator.constants',
      version='1.0',
      description='Gelato constants',
      namespace_packages=['gelato'],
      long_description='',
      author='',
      author_email='',
      license='',
      url='',
      include_package_data=True,
      packages=find_packages(exclude=['tests']),
      install_requires=['django', 'tower',])
