from unittest import expectedFailure
from .. utils import CSSWGTestCase

class test_CssPseudo4(CSSWGTestCase):
    def test_first_letter_001(self):
        self.assertRender('test_CssPseudo4', 'first_letter_001')

    def test_first_letter_002(self):
        self.assertRender('test_CssPseudo4', 'first_letter_002')

    def test_first_letter_003(self):
        self.assertRender('test_CssPseudo4', 'first_letter_003')

