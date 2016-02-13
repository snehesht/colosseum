from unittest import expectedFailure
from .. utils import CSSWGTestCase

class test_CssStyleAttr1(CSSWGTestCase):
    def test_style_attr_braces_001(self):
        self.assertRender('test_CssStyleAttr1', 'style_attr_braces_001')

    def test_style_attr_braces_002_quirks(self):
        self.assertRender('test_CssStyleAttr1', 'style_attr_braces_002_quirks')

    def test_style_attr_braces_002(self):
        self.assertRender('test_CssStyleAttr1', 'style_attr_braces_002')

    def test_style_attr_braces_003(self):
        self.assertRender('test_CssStyleAttr1', 'style_attr_braces_003')

    def test_style_attr_cascade_001(self):
        self.assertRender('test_CssStyleAttr1', 'style_attr_cascade_001')

    def test_style_attr_cascade_002(self):
        self.assertRender('test_CssStyleAttr1', 'style_attr_cascade_002')

    def test_style_attr_cascade_003(self):
        self.assertRender('test_CssStyleAttr1', 'style_attr_cascade_003')

    def test_style_attr_cascade_004(self):
        self.assertRender('test_CssStyleAttr1', 'style_attr_cascade_004')

    def test_style_attr_cascade_005(self):
        self.assertRender('test_CssStyleAttr1', 'style_attr_cascade_005')

    def test_style_attr_cascade_006(self):
        self.assertRender('test_CssStyleAttr1', 'style_attr_cascade_006')

    def test_style_attr_cascade_007(self):
        self.assertRender('test_CssStyleAttr1', 'style_attr_cascade_007')

    def test_style_attr_specificity_001(self):
        self.assertRender('test_CssStyleAttr1', 'style_attr_specificity_001')

    def test_style_attr_specificity_002(self):
        self.assertRender('test_CssStyleAttr1', 'style_attr_specificity_002')

    def test_style_attr_urls_001(self):
        self.assertRender('test_CssStyleAttr1', 'style_attr_urls_001')

    def test_style_attr_urls_002(self):
        self.assertRender('test_CssStyleAttr1', 'style_attr_urls_002')

