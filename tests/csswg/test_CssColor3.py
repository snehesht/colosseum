from unittest import expectedFailure
from .. utils import CSSWGTestCase

class test_CssColor3(CSSWGTestCase):
    def test_t31_color_currentcolor_b(self):
        self.assertRender('test_CssColor3', 't31_color_currentcolor_b')

    def test_t31_color_text_a(self):
        self.assertRender('test_CssColor3', 't31_color_text_a')

    def test_t32_opacity_basic_0_0_a(self):
        self.assertRender('test_CssColor3', 't32_opacity_basic_0_0_a')

    def test_t32_opacity_basic_0_6_a(self):
        self.assertRender('test_CssColor3', 't32_opacity_basic_0_6_a')

    def test_t32_opacity_basic_1_0_a(self):
        self.assertRender('test_CssColor3', 't32_opacity_basic_1_0_a')

    def test_t32_opacity_clamping_0_0_b(self):
        self.assertRender('test_CssColor3', 't32_opacity_clamping_0_0_b')

    def test_t32_opacity_clamping_1_0_b(self):
        self.assertRender('test_CssColor3', 't32_opacity_clamping_1_0_b')

    def test_t32_opacity_offscreen_b(self):
        self.assertRender('test_CssColor3', 't32_opacity_offscreen_b')

    def test_t32_opacity_offscreen_multiple_boxes_1_c(self):
        self.assertRender('test_CssColor3', 't32_opacity_offscreen_multiple_boxes_1_c')

    def test_t32_opacity_offscreen_multiple_boxes_2_c(self):
        self.assertRender('test_CssColor3', 't32_opacity_offscreen_multiple_boxes_2_c')

    def test_t32_opacity_offscreen_with_alpha_c(self):
        self.assertRender('test_CssColor3', 't32_opacity_offscreen_with_alpha_c')

    def test_t32_opacity_zorder_c(self):
        self.assertRender('test_CssColor3', 't32_opacity_zorder_c')

    def test_t41_html4_keywords_a(self):
        self.assertRender('test_CssColor3', 't41_html4_keywords_a')

    def test_t421_rgb_clip_outside_gamut_b(self):
        self.assertRender('test_CssColor3', 't421_rgb_clip_outside_gamut_b')

    def test_t421_rgb_func_int_a(self):
        self.assertRender('test_CssColor3', 't421_rgb_func_int_a')

    def test_t421_rgb_func_no_mixed_f(self):
        self.assertRender('test_CssColor3', 't421_rgb_func_no_mixed_f')

    def test_t421_rgb_func_pct_a(self):
        self.assertRender('test_CssColor3', 't421_rgb_func_pct_a')

    def test_t421_rgb_func_whitespace_b(self):
        self.assertRender('test_CssColor3', 't421_rgb_func_whitespace_b')

    def test_t421_rgb_hex_parsing_f(self):
        self.assertRender('test_CssColor3', 't421_rgb_hex_parsing_f')

    def test_t421_rgb_hex3_a(self):
        self.assertRender('test_CssColor3', 't421_rgb_hex3_a')

    def test_t421_rgb_hex3_expand_b(self):
        self.assertRender('test_CssColor3', 't421_rgb_hex3_expand_b')

    def test_t421_rgb_hex6_a(self):
        self.assertRender('test_CssColor3', 't421_rgb_hex6_a')

    def test_t421_rgb_values_meaning_b(self):
        self.assertRender('test_CssColor3', 't421_rgb_values_meaning_b')

    def test_t422_rgba_a0_0_a(self):
        self.assertRender('test_CssColor3', 't422_rgba_a0_0_a')

    def test_t422_rgba_a0_6_a(self):
        self.assertRender('test_CssColor3', 't422_rgba_a0_6_a')

    def test_t422_rgba_a1_0_a(self):
        self.assertRender('test_CssColor3', 't422_rgba_a1_0_a')

    def test_t422_rgba_clamping_a0_0_b(self):
        self.assertRender('test_CssColor3', 't422_rgba_clamping_a0_0_b')

    def test_t422_rgba_clamping_a1_0_b(self):
        self.assertRender('test_CssColor3', 't422_rgba_clamping_a1_0_b')

    def test_t422_rgba_clip_outside_device_gamut_b(self):
        self.assertRender('test_CssColor3', 't422_rgba_clip_outside_device_gamut_b')

    def test_t422_rgba_func_int_a(self):
        self.assertRender('test_CssColor3', 't422_rgba_func_int_a')

    def test_t422_rgba_func_no_mixed_f(self):
        self.assertRender('test_CssColor3', 't422_rgba_func_no_mixed_f')

    def test_t422_rgba_func_pct_a(self):
        self.assertRender('test_CssColor3', 't422_rgba_func_pct_a')

    def test_t422_rgba_func_whitespace_b(self):
        self.assertRender('test_CssColor3', 't422_rgba_func_whitespace_b')

    def test_t422_rgba_onscreen_b(self):
        self.assertRender('test_CssColor3', 't422_rgba_onscreen_b')

    def test_t422_rgba_onscreen_multiple_boxes_c(self):
        self.assertRender('test_CssColor3', 't422_rgba_onscreen_multiple_boxes_c')

    def test_t422_rgba_values_meaning_b(self):
        self.assertRender('test_CssColor3', 't422_rgba_values_meaning_b')

    def test_t423_transparent_1_a(self):
        self.assertRender('test_CssColor3', 't423_transparent_1_a')

    def test_t423_transparent_2_a(self):
        self.assertRender('test_CssColor3', 't423_transparent_2_a')

    def test_t424_hsl_basic_a(self):
        self.assertRender('test_CssColor3', 't424_hsl_basic_a')

    def test_t424_hsl_clip_outside_gamut_b(self):
        self.assertRender('test_CssColor3', 't424_hsl_clip_outside_gamut_b')

    def test_t424_hsl_h_rotating_b(self):
        self.assertRender('test_CssColor3', 't424_hsl_h_rotating_b')

    def test_t424_hsl_parsing_f(self):
        self.assertRender('test_CssColor3', 't424_hsl_parsing_f')

    def test_t424_hsl_values_b_1(self):
        self.assertRender('test_CssColor3', 't424_hsl_values_b_1')

    def test_t424_hsl_values_b_10(self):
        self.assertRender('test_CssColor3', 't424_hsl_values_b_10')

    def test_t424_hsl_values_b_11(self):
        self.assertRender('test_CssColor3', 't424_hsl_values_b_11')

    def test_t424_hsl_values_b_12(self):
        self.assertRender('test_CssColor3', 't424_hsl_values_b_12')

    def test_t424_hsl_values_b_13(self):
        self.assertRender('test_CssColor3', 't424_hsl_values_b_13')

    def test_t424_hsl_values_b_14(self):
        self.assertRender('test_CssColor3', 't424_hsl_values_b_14')

    def test_t424_hsl_values_b_15(self):
        self.assertRender('test_CssColor3', 't424_hsl_values_b_15')

    def test_t424_hsl_values_b_2(self):
        self.assertRender('test_CssColor3', 't424_hsl_values_b_2')

    def test_t424_hsl_values_b_3(self):
        self.assertRender('test_CssColor3', 't424_hsl_values_b_3')

    def test_t424_hsl_values_b_4(self):
        self.assertRender('test_CssColor3', 't424_hsl_values_b_4')

    def test_t424_hsl_values_b_5(self):
        self.assertRender('test_CssColor3', 't424_hsl_values_b_5')

    def test_t424_hsl_values_b_6(self):
        self.assertRender('test_CssColor3', 't424_hsl_values_b_6')

    def test_t424_hsl_values_b_7(self):
        self.assertRender('test_CssColor3', 't424_hsl_values_b_7')

    def test_t424_hsl_values_b_8(self):
        self.assertRender('test_CssColor3', 't424_hsl_values_b_8')

    def test_t424_hsl_values_b_9(self):
        self.assertRender('test_CssColor3', 't424_hsl_values_b_9')

    def test_t425_hsla_basic_a(self):
        self.assertRender('test_CssColor3', 't425_hsla_basic_a')

    def test_t425_hsla_clip_outside_device_gamut_b(self):
        self.assertRender('test_CssColor3', 't425_hsla_clip_outside_device_gamut_b')

    def test_t425_hsla_h_rotating_b(self):
        self.assertRender('test_CssColor3', 't425_hsla_h_rotating_b')

    def test_t425_hsla_onscreen_b(self):
        self.assertRender('test_CssColor3', 't425_hsla_onscreen_b')

    def test_t425_hsla_onscreen_multiple_boxes_c(self):
        self.assertRender('test_CssColor3', 't425_hsla_onscreen_multiple_boxes_c')

    def test_t425_hsla_parsing_f(self):
        self.assertRender('test_CssColor3', 't425_hsla_parsing_f')

    def test_t425_hsla_values_b(self):
        self.assertRender('test_CssColor3', 't425_hsla_values_b')

    def test_t43_svg_keywords_a(self):
        self.assertRender('test_CssColor3', 't43_svg_keywords_a')

    def test_t44_currentcolor_background_b(self):
        self.assertRender('test_CssColor3', 't44_currentcolor_background_b')

    def test_t44_currentcolor_border_b(self):
        self.assertRender('test_CssColor3', 't44_currentcolor_border_b')

    def test_t44_currentcolor_inherited_c(self):
        self.assertRender('test_CssColor3', 't44_currentcolor_inherited_c')

    def test_t451_system_colors_a(self):
        self.assertRender('test_CssColor3', 't451_system_colors_a')

    def test_will_change_stacking_context_opacity_1(self):
        self.assertRender('test_CssColor3', 'will_change_stacking_context_opacity_1')

