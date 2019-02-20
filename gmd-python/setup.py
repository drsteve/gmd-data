import os
import glob

os.environ['DISTUTILS_DEBUG'] = "1"

from setuptools import setup, find_packages
from setuptools.command import install as _install

setup(name='gmd-python',
      version = "0.99",
      description = "GMD-Python",
      author = "Various",
      author_email = 'None',
      url = "",
      download_url = "",
      long_description = "Python API to GMD-data PostgreSQL database",
      install_requires=['numpy', 'matplotlib', 'sqlalchemy', 'psycopg2'],
      packages=find_packages(),
      license='BSD',
      zip_safe = False,
      classifiers = [
            "Development Status :: 4 - Beta",
            "Topic :: Scientific/Engineering",
            "Intended Audience :: Science/Research",
            "Natural Language :: English",
            "Programming Language :: Python"
            ]
      )
