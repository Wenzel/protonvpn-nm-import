#!/usr/bin/env python3

import os
from setuptools import setup


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(
    name='protonvpn-nm-import',
    version='0.1',
    description='ProtonVPN NetworkManager import script',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    author='Mathieu Tarral',
    author_email='mathieu.tarral@protonmail.com',
    url='https://github.com/Wenzel/protonvpn-nm-import',
    python_requires='>=3.4',
    setup_requires=[''],
    install_requires=['docopt'],
    tests_require=["pytest-pep8"],
    entry_points={
        'console_scripts': ['protonvpn-nm-import=protonvpn-nm-import:main'],
    }
)
