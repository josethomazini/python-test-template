'''
Messages in many idioms.
'''

from sources.core.settings import LANG, SETTINGS

MESSAGE = {
    'div_by_zero_forbidden': {
        LANG.PT_BR: 'Divisão por zero é proibida!',
        LANG.EN_US: 'Division by zero is forbidden!',
    },
}

def _(key):
    return MESSAGE[key][SETTINGS['LANGUAGE']]
