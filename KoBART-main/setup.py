# coding=utf-8
# Modified MIT License

# Software Copyright (c) 2020 SK telecom

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
# The above copyright notice and this permission notice need not be included
# with content created by the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.

from setuptools import find_packages, setup

setup(name='kobart',
      version=0.4,
      url='https://github.com/SKT-AI/KoBART.git',
      license='midified MIT',
      author='Woocheol Jeong',
      author_email='oocheol1@gmail.com',
      description='KoBART (Korean BART)',
      packages=find_packages(where=".", exclude=(
          'tests',
          'scripts',
          'examples'
      )),
      long_description=open('KoBART-main/README.md', encoding='utf-8').read(),
      zip_safe=False,
      include_package_data=True,
      install_requires=[
          'transformers == 4.3.3',
          'torch == 1.7.1'
      ]
      )
