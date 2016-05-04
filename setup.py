import os.path
import re
from setuptools import setup, find_packages


ROOT_DIR = os.path.dirname(__file__)


def read_contents(local_filepath):
    with open(os.path.join(ROOT_DIR, local_filepath)) as f:
        return f.read()


def get_requirements(requirements_filepath):
    '''
    Return list of this package requirements via local filepath.
    '''
    return read_contents(requirements_filepath).split('\n')


def get_version(package):
    '''
    Return package version as listed in `__version__` in `init.py`.
    '''
    init_py = read_contents(os.path.join(package, '__init__.py'))
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_long_description(markdown_filepath):
    '''
    Return the long description in RST format, when possible.
    '''
    try:
        import pypandoc
        return pypandoc.convert(markdown_filepath, 'rst')
    except ImportError:
        return read_contents(markdown_filepath)


setup(
    name='argparse-manpager',
    version=get_version('manpager'),
    packages=find_packages(exclude=['tests.*', 'tests', 'waftools.*', 'waftools']),
    author='XZS',
    author_email='d.f.fischer@web.de',
    description=(
        'Generate man pages from argparse'
    ),
    license='GPLv3',
    keywords=' '.join((
        'argparse',
        'man',
        'manpages',
    )),
    long_description=get_long_description('README.md'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Documentation',
    ],
    install_requires=[],
    url='https://github.com/dffischer/argparse-manpager',
)
