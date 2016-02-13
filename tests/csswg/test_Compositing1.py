from unittest import expectedFailure
from .. utils import CSSWGTestCase

class test_Compositing1(CSSWGTestCase):
    def test_blend_isolation(self):
        self.assertRender('test_Compositing1', 'blend_isolation')

    def test_blending_in_a_group_with_filter(self):
        self.assertRender('test_Compositing1', 'blending_in_a_group_with_filter')

    def test_blending_in_a_group_with_opacity(self):
        self.assertRender('test_Compositing1', 'blending_in_a_group_with_opacity')

    def test_line_with_svg_background(self):
        self.assertRender('test_Compositing1', 'line_with_svg_background')

    def test_text_with_svg_background(self):
        self.assertRender('test_Compositing1', 'text_with_svg_background')

    def test_text_with_svg_background(self):
        self.assertRender('test_Compositing1', 'text_with_svg_background')

    def test_will_change_stacking_context_isolation_1(self):
        self.assertRender('test_Compositing1', 'will_change_stacking_context_isolation_1')

    def test_will_change_stacking_context_mix_blend_mode_1(self):
        self.assertRender('test_Compositing1', 'will_change_stacking_context_mix_blend_mode_1')

