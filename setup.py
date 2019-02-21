#!/usr/bin/python3
"""Setup
"""
#import distutils.cmd
import re
from setuptools import setup, find_packages

# import build
# import src.bankparser


# class GenFiles(distutils.cmd.Command):
#     """Генерация некоторых файлов проекта и справки
#     """
#     user_options = []
#     description = 'generate .py and readme command'
#
#     def initialize_options(self):
#         pass
#
#     def finalize_options(self):
#         pass
#
#     def run(self):
#         mybuild = build.MyBuild()
#         mybuild.buid()
#
#
# class CopyScript(distutils.cmd.Command):
#     """
#     Для отладочных целей. Копирует пакет без установки в указанный каталог
#     """
#     user_options = [('pubdir=', None, 'Specify dir for public')]
#     description = 'copy script for testing'
#
#     def initialize_options(self):
#         self.pubdir = None
#
#     def finalize_options(self):
#         pass
#
#     def run(self):
#         mybuild = build.MyBuild(self.pubdir)
#         mybuild.copy_script()

# find version in init file
def find_version(filename):
    with open(filename, 'r') as f:
        version_file = f.read()
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                                  version_file, re.M)
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find version string.")

version = find_version("src/bankparser/__init__.py")

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(name='bankparser',
      version=version,
      author="partizand",
      author_email="",
      url="https://github.com/partizand/bankparser",
      description="Convert banks statements to qif format",
      long_description=long_description,
      license="GPLv3",
      keywords=["qif", "banking", "statement"],

      #cmdclass={'copyscript': CopyScript, 'genfiles': GenFiles},

      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 3',
          'Natural Language :: Russian',
          'Topic :: Office/Business :: Financial :: Accounting',
          'Topic :: Utilities',
          'Environment :: Console',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: GNU General Public License v3'],

      #packages=find_packages('src'),

      #packages=['bankparser', 'bankparser.banks', 'bankparser.test'],
      packages=['bankparser', 'bankparser.banks'],

      package_dir={'': 'src'},

      #package_data={'bankparser': ['*.ini']},

      test_suite='bankparser.test',

      install_requires=['setuptools'],
      #                   'appdirs'
      #                   ],
      # namespace_packages=["bankparser"],

      entry_points={
          'console_scripts':
              ['bankparser = bankparser.bankparsercli:main'],
      },
      #include_package_data=True,
      #zip_safe=False
      )
