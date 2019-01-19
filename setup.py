"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
"""

from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='erebusfall',

    version='0.0.3',

    description='Apply a simple ice-volume correction to marine-isotope proxy records in Python',
    long_description=readme(),
    long_description_content_type='text/markdown',

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
