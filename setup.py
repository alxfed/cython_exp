from setuptools import setup, Extension

module = Extension ('example', sources=['example.pyx'])

setup(
    name='cython_exp',
    version='0.0.1',
    url='https://github.com/alxfed/cython_exp',
    author='alxfed',
    description='Cython experiments',
    ext_modules=[module]
)
