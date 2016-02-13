from unittest import expectedFailure
from .. utils import CSSWGTestCase

class test_Selectors4(CSSWGTestCase):
    def test_focus_within_001(self):
        self.assertRender('test_Selectors4', 'focus_within_001')

    def test_focus_within_002(self):
        self.assertRender('test_Selectors4', 'focus_within_002')

    def test_focus_within_003(self):
        self.assertRender('test_Selectors4', 'focus_within_003')

    def test_focus_within_004(self):
        self.assertRender('test_Selectors4', 'focus_within_004')

    def test_focus_within_005(self):
        self.assertRender('test_Selectors4', 'focus_within_005')

    def test_focus_within_006(self):
        self.assertRender('test_Selectors4', 'focus_within_006')

    def test_focus_within_shadow_001(self):
        self.assertRender('test_Selectors4', 'focus_within_shadow_001')

    def test_focus_within_shadow_002(self):
        self.assertRender('test_Selectors4', 'focus_within_shadow_002')

    def test_focus_within_shadow_003(self):
        self.assertRender('test_Selectors4', 'focus_within_shadow_003')

    def test_focus_within_shadow_004(self):
        self.assertRender('test_Selectors4', 'focus_within_shadow_004')

    def test_focus_within_shadow_005(self):
        self.assertRender('test_Selectors4', 'focus_within_shadow_005')

    def test_hover_001_manual(self):
        self.assertRender('test_Selectors4', 'hover_001_manual')

    def test_selector_required(self):
        self.assertRender('test_Selectors4', 'selector_required')

    def test_selectors_dir_selector_ltr_001(self):
        self.assertRender('test_Selectors4', 'selectors_dir_selector_ltr_001')

    def test_selectors_dir_selector_rtl_001(self):
        self.assertRender('test_Selectors4', 'selectors_dir_selector_rtl_001')

