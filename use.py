# -*- coding: utf-8 -*-
"""...
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
