#!/usr/bin/env python
"""
Example
"""

import os

import GhostInspector


def TESTING():
    c = GhostInspector.Client(api_key='35d22edc556e5b88f1e1bcf8fd3c90da7c0056c2')
    print(c.get_tests())

if __name__ == '__main__':
    TESTING()
