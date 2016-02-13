from unittest import expectedFailure
from .. utils import CSSWGTestCase

class test_CssExclusions1(CSSWGTestCase):
    def test_exclusions_wrap_flow_01(self):
        self.assertRender('test_CssExclusions1', 'exclusions_wrap_flow_01')

    def test_exclusions_wrap_flow_02(self):
        self.assertRender('test_CssExclusions1', 'exclusions_wrap_flow_02')

    def test_exclusions_wrap_flow_03(self):
        self.assertRender('test_CssExclusions1', 'exclusions_wrap_flow_03')

    def test_exclusions_wrap_flow_04(self):
        self.assertRender('test_CssExclusions1', 'exclusions_wrap_flow_04')

    def test_wrap_flow_001(self):
        self.assertRender('test_CssExclusions1', 'wrap_flow_001')

    def test_wrap_flow_002(self):
        self.assertRender('test_CssExclusions1', 'wrap_flow_002')

    def test_wrap_flow_003(self):
        self.assertRender('test_CssExclusions1', 'wrap_flow_003')

    def test_wrap_flow_004(self):
        self.assertRender('test_CssExclusions1', 'wrap_flow_004')

    def test_wrap_flow_005(self):
        self.assertRender('test_CssExclusions1', 'wrap_flow_005')

    def test_wrap_flow_006(self):
        self.assertRender('test_CssExclusions1', 'wrap_flow_006')

    def test_wrap_through_001(self):
        self.assertRender('test_CssExclusions1', 'wrap_through_001')

