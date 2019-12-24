'''
Settings for this aplication.

All other packages must search for the language defined into this core settings
module.
'''

from enum import Enum

class LANG(Enum):
    PT_BR = 'PT_BR'
    EN_US = 'EN_US'

SETTINGS = {
    'LANGUAGE': LANG.PT_BR,
}
