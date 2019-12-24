'''
Tests for the messages module.
'''

import pytest

from sources.core.settings import SETTINGS, LANG
from sources.core.messages import MESSAGE, _


def test_all_language_messages_exists_for_core():
    '''
    If a language is defined in the enum LANG, then the MESSAGE dict must
    provide that language for all of its messages.
    '''
    for _, msg in MESSAGE.items():
        for idiom in LANG:
            assert idiom in msg  # it exists!
            assert msg[idiom] # it is neither '' nor None

@pytest.mark.parametrize('lang, phrase', [
    (LANG.EN_US, 'Division by zero is forbidden!'),
    (LANG.PT_BR, 'Divisão por zero é proibida!'),
])
def test_language_div_by_zero_forbidden(lang, phrase):
    SETTINGS['LANGUAGE'] = lang
    result = _('div_by_zero_forbidden')
    assert result == phrase
