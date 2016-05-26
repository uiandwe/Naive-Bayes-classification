__author__ = 'hyeonsj'

import pytest
import word_decision


def test_answer():
    assert word_decision.get_input_file() == "[('너', 'NP'), ('는', 'JX'), ('아름답', 'VA'), ('다', 'EFN'), ('.', 'SF')]"


def test_sentence_to_kkma():
    assert word_decision.sentence_to_kkma("그녀는 아릅답다.") == "[('너', 'NP'), ('는', 'JX'), ('아름답', 'VA'), ('다', 'EFN'), ('.', 'SF')]"


def test_run_word_decision():
    assert word_decision.run_word_decision([('너', 'NP'), ('는', 'JX'), ('아름답', 'VA'), ('다', 'EFN'), ('.', 'SF')]) == \
           "['긍정', ('너', 'NP'), ('는', 'JX'), ('아름답', 'VA'), ('다', 'EFN'), ('.', 'SF')]"