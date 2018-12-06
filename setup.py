from setuptools import find_packages, setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='sudoku-solver',
      version='0.1',
      description='Simple Sudoku solver',
      long_description=readme(),
      url='https://github.com/yitsushi/sudoku-solver',
      author='Balazs Nadasdi',
      author_email='yitsushi@gmail.com',
      license='MIT',
      packages=['sudoku_solver'],
      zip_safe=False,
)
