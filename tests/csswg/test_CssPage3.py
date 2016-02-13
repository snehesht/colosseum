from unittest import expectedFailure
from .. utils import CSSWGTestCase

class test_CssPage3(CSSWGTestCase):
    def test_allowed_page_breaks_001a(self):
        self.assertRender('test_CssPage3', 'allowed_page_breaks_001a')

    def test_allowed_page_breaks_001b(self):
        self.assertRender('test_CssPage3', 'allowed_page_breaks_001b')

    def test_allowed_page_breaks_001c(self):
        self.assertRender('test_CssPage3', 'allowed_page_breaks_001c')

    def test_at_page_rule_002_a(self):
        self.assertRender('test_CssPage3', 'at_page_rule_002_a')

    def test_at_page_rule_002_b(self):
        self.assertRender('test_CssPage3', 'at_page_rule_002_b')

    def test_at_page_rule_002_c(self):
        self.assertRender('test_CssPage3', 'at_page_rule_002_c')

    def test_orphans_001(self):
        self.assertRender('test_CssPage3', 'orphans_001')

    def test_orphans_004a(self):
        self.assertRender('test_CssPage3', 'orphans_004a')

    def test_orphans_004b(self):
        self.assertRender('test_CssPage3', 'orphans_004b')

    def test_page_background_000(self):
        self.assertRender('test_CssPage3', 'page_background_000')

    def test_page_borders_000(self):
        self.assertRender('test_CssPage3', 'page_borders_000')

    def test_page_box_000(self):
        self.assertRender('test_CssPage3', 'page_box_000')

    def test_page_break_after_002(self):
        self.assertRender('test_CssPage3', 'page_break_after_002')

    def test_page_break_after_005(self):
        self.assertRender('test_CssPage3', 'page_break_after_005')

    def test_page_break_after_006(self):
        self.assertRender('test_CssPage3', 'page_break_after_006')

    def test_page_break_after_007(self):
        self.assertRender('test_CssPage3', 'page_break_after_007')

    def test_page_break_after_008(self):
        self.assertRender('test_CssPage3', 'page_break_after_008')

    def test_page_break_after_009(self):
        self.assertRender('test_CssPage3', 'page_break_after_009')

    def test_page_break_after_010(self):
        self.assertRender('test_CssPage3', 'page_break_after_010')

    def test_page_break_before_000(self):
        self.assertRender('test_CssPage3', 'page_break_before_000')

    def test_page_break_before_003(self):
        self.assertRender('test_CssPage3', 'page_break_before_003')

    def test_page_break_before_004(self):
        self.assertRender('test_CssPage3', 'page_break_before_004')

    def test_page_break_before_005(self):
        self.assertRender('test_CssPage3', 'page_break_before_005')

    def test_page_break_before_006(self):
        self.assertRender('test_CssPage3', 'page_break_before_006')

    def test_page_break_before_007_b(self):
        self.assertRender('test_CssPage3', 'page_break_before_007_b')

    def test_page_break_before_007(self):
        self.assertRender('test_CssPage3', 'page_break_before_007')

    def test_page_break_before_008(self):
        self.assertRender('test_CssPage3', 'page_break_before_008')

    def test_page_break_before_009(self):
        self.assertRender('test_CssPage3', 'page_break_before_009')

    def test_page_break_before_010(self):
        self.assertRender('test_CssPage3', 'page_break_before_010')

    def test_page_break_before_011(self):
        self.assertRender('test_CssPage3', 'page_break_before_011')

    def test_page_break_before_020(self):
        self.assertRender('test_CssPage3', 'page_break_before_020')

    def test_page_break_inside_001(self):
        self.assertRender('test_CssPage3', 'page_break_inside_001')

    def test_page_break_inside_004(self):
        self.assertRender('test_CssPage3', 'page_break_inside_004')

    def test_page_break_margins_003(self):
        self.assertRender('test_CssPage3', 'page_break_margins_003')

    def test_page_break_margins_004(self):
        self.assertRender('test_CssPage3', 'page_break_margins_004')

    def test_page_breaks_100(self):
        self.assertRender('test_CssPage3', 'page_breaks_100')

    def test_page_breaks_101(self):
        self.assertRender('test_CssPage3', 'page_breaks_101')

    def test_page_container_000(self):
        self.assertRender('test_CssPage3', 'page_container_000')

    def test_page_container_001(self):
        self.assertRender('test_CssPage3', 'page_container_001')

    def test_page_container_002(self):
        self.assertRender('test_CssPage3', 'page_container_002')

    def test_page_container_003(self):
        self.assertRender('test_CssPage3', 'page_container_003')

    def test_page_container_004(self):
        self.assertRender('test_CssPage3', 'page_container_004')

    def test_page_container_005(self):
        self.assertRender('test_CssPage3', 'page_container_005')

    def test_page_container_006(self):
        self.assertRender('test_CssPage3', 'page_container_006')

    def test_page_container_008(self):
        self.assertRender('test_CssPage3', 'page_container_008')

    def test_page_container_009(self):
        self.assertRender('test_CssPage3', 'page_container_009')

    def test_page_container_010(self):
        self.assertRender('test_CssPage3', 'page_container_010')

    def test_page_counters_000(self):
        self.assertRender('test_CssPage3', 'page_counters_000')

    def test_page_grammar_001(self):
        self.assertRender('test_CssPage3', 'page_grammar_001')

    def test_page_grammar_002(self):
        self.assertRender('test_CssPage3', 'page_grammar_002')

    def test_page_margin_000(self):
        self.assertRender('test_CssPage3', 'page_margin_000')

    def test_page_margin_001(self):
        self.assertRender('test_CssPage3', 'page_margin_001')

    def test_page_margin_002(self):
        self.assertRender('test_CssPage3', 'page_margin_002')

    def test_page_margin_003(self):
        self.assertRender('test_CssPage3', 'page_margin_003')

    def test_page_name_000(self):
        self.assertRender('test_CssPage3', 'page_name_000')

    def test_page_properties_000(self):
        self.assertRender('test_CssPage3', 'page_properties_000')

    def test_page_props_100_a(self):
        self.assertRender('test_CssPage3', 'page_props_100_a')

    def test_page_props_100_b(self):
        self.assertRender('test_CssPage3', 'page_props_100_b')

    def test_page_props_101(self):
        self.assertRender('test_CssPage3', 'page_props_101')

    def test_page_props_103(self):
        self.assertRender('test_CssPage3', 'page_props_103')

    def test_page_selectors_001(self):
        self.assertRender('test_CssPage3', 'page_selectors_001')

    def test_page_selectors_002(self):
        self.assertRender('test_CssPage3', 'page_selectors_002')

    def test_page_selectors_003(self):
        self.assertRender('test_CssPage3', 'page_selectors_003')

    def test_page_selectors_004(self):
        self.assertRender('test_CssPage3', 'page_selectors_004')

    def test_page_selectors_006(self):
        self.assertRender('test_CssPage3', 'page_selectors_006')

    def test_page_size_000(self):
        self.assertRender('test_CssPage3', 'page_size_000')

    def test_page_size_001(self):
        self.assertRender('test_CssPage3', 'page_size_001')

    def test_page_size_002(self):
        self.assertRender('test_CssPage3', 'page_size_002')

    def test_page_size_003(self):
        self.assertRender('test_CssPage3', 'page_size_003')

    def test_page_size_004(self):
        self.assertRender('test_CssPage3', 'page_size_004')

    def test_page_size_005(self):
        self.assertRender('test_CssPage3', 'page_size_005')

    def test_page_size_006(self):
        self.assertRender('test_CssPage3', 'page_size_006')

    def test_page_size_007(self):
        self.assertRender('test_CssPage3', 'page_size_007')

    def test_page_size_008(self):
        self.assertRender('test_CssPage3', 'page_size_008')

    def test_page_size_009(self):
        self.assertRender('test_CssPage3', 'page_size_009')

    def test_page_size_010(self):
        self.assertRender('test_CssPage3', 'page_size_010')

    def test_widows_004a(self):
        self.assertRender('test_CssPage3', 'widows_004a')

    def test_widows_004b(self):
        self.assertRender('test_CssPage3', 'widows_004b')

