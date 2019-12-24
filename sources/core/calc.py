'''
Great calc functions.
'''

from sources.core.exceptions import DivByZeroException


def sub(a, b):
    return a - b

def add(a, b):
    return a + b

def div(a, b):
    if b == 0:
        raise DivByZeroException
    return a / b

def mul(a, b):
    return a * b
