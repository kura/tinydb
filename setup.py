# coding=utf-8
from setuptools import setup, find_packages
from codecs import open
import os


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    return open(path, encoding='utf-8').read()


setup(
    name="tinydb",
    version="2.3.2",
    packages=find_packages(),

    # development metadata
    zip_safe=True,

    # metadata for upload to PyPI
    author="Markus Siemens",
    author_email="markus@m-siemens.de",
    description="TinyDB is a tiny, document oriented database optimized for "
                "your happiness :)",
    license="MIT",
    keywords="database nosql",
    url="https://github.com/msiemens/tinydb",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Topic :: Database",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent"
    ],

    long_description=read('README.rst'),
)
