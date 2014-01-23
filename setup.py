from __future__ import unicode_literals, absolute_import

from setuptools import setup, find_packages


setup(
    name='gro',
    version='0.0.0',
    url='https://github.com/txomon/grooveshark-python',
    license='MIT',
    author='Javier Domingo Cansino',
    author_email='javierdo1@gmail.com',
    description='Grooveshark API binding for Python',
    long_description=open('README.md').read(),
    packages=find_packages(),
    include_package_data=True,
)
