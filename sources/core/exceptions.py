'''
Exceptions for core.
'''

from sources.core.messages import _

class DivByZeroException(Exception):
    def __init__(self):
        txt = _('div_by_zero_forbidden')
        super().__init__(txt)
