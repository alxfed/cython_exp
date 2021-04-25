# -*- coding: utf-8 -*-
"""
http://docs.cython.org/en/latest/src/quickstart/build.html#building-a-cython-module-using-setuptools
https://www.jetbrains.com/help/pycharm/2021.1/cython.html#get-started-cython
"""
from example import function


def main() -> bool:
    print(function(2, 2))
    return True


if __name__ == '__main__':
    if main():
        print('Done!')
    else:
        print('Not done...')
