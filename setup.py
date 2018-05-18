"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
"""

from setuptools import setup, find_packages
# To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='erebusfall',

    version='0.0.2',

    description='Ice-volume correction to marine-isotope proxy records in Python',

    url='https://github.com/brews/erebusfall',

    author='S. Brewster Malevich',
    author_email='malevich@email.arizona.edu',

    license='GPLv3',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',

        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Programming Language :: Python :: 3',
    ],

    keywords='marine isotope paleoclimate proxy deuterium d18o',
    packages=find_packages(exclude=['contrib', 'docs']),
    install_requires=['numpy', 'scipy'],
    tests_require=['pytest'],
    package_data={'erebusfall': ['benthic_stacks/*.csv']},
)
