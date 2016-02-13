from unittest import expectedFailure
from .. utils import CSSWGTestCase

class test_Filters1(CSSWGTestCase):
    def test_css_filters_animation_blur(self):
        self.assertRender('test_Filters1', 'css_filters_animation_blur')

    def test_css_filters_animation_brightness(self):
        self.assertRender('test_Filters1', 'css_filters_animation_brightness')

    def test_css_filters_animation_combined_001(self):
        self.assertRender('test_Filters1', 'css_filters_animation_combined_001')

    def test_css_filters_animation_contrast(self):
        self.assertRender('test_Filters1', 'css_filters_animation_contrast')

    def test_css_filters_animation_drop_shadow(self):
        self.assertRender('test_Filters1', 'css_filters_animation_drop_shadow')

    def test_css_filters_animation_grayscale(self):
        self.assertRender('test_Filters1', 'css_filters_animation_grayscale')

    def test_css_filters_animation_hue_rotate(self):
        self.assertRender('test_Filters1', 'css_filters_animation_hue_rotate')

    def test_css_filters_animation_invert(self):
        self.assertRender('test_Filters1', 'css_filters_animation_invert')

    def test_css_filters_animation_opacity(self):
        self.assertRender('test_Filters1', 'css_filters_animation_opacity')

    def test_css_filters_animation_saturate(self):
        self.assertRender('test_Filters1', 'css_filters_animation_saturate')

    def test_css_filters_animation_sepia(self):
        self.assertRender('test_Filters1', 'css_filters_animation_sepia')

    def test_fecolormatrix_type(self):
        self.assertRender('test_Filters1', 'fecolormatrix_type')

    def test_filter_contrast_001(self):
        self.assertRender('test_Filters1', 'filter_contrast_001')

    def test_filter_contrast_002(self):
        self.assertRender('test_Filters1', 'filter_contrast_002')

    def test_filter_contrast_003(self):
        self.assertRender('test_Filters1', 'filter_contrast_003')

    def test_filter_external_001_test(self):
        self.assertRender('test_Filters1', 'filter_external_001_test')

    def test_filter_external_002_test(self):
        self.assertRender('test_Filters1', 'filter_external_002_test')

    def test_filter_grayscale_001(self):
        self.assertRender('test_Filters1', 'filter_grayscale_001')

    def test_filter_hue_rotate_001_test(self):
        self.assertRender('test_Filters1', 'filter_hue_rotate_001_test')

    def test_filter_invert_001_test(self):
        self.assertRender('test_Filters1', 'filter_invert_001_test')

    def test_filter_invert_002_test(self):
        self.assertRender('test_Filters1', 'filter_invert_002_test')

    def test_filter_saturate_001_test(self):
        self.assertRender('test_Filters1', 'filter_saturate_001_test')

    def test_filters_drop_shadow(self):
        self.assertRender('test_Filters1', 'filters_drop_shadow')

    def test_filters_grayscale_001_test(self):
        self.assertRender('test_Filters1', 'filters_grayscale_001_test')

    def test_filters_opacity_001_test(self):
        self.assertRender('test_Filters1', 'filters_opacity_001_test')

    def test_filters_opacity_002_test(self):
        self.assertRender('test_Filters1', 'filters_opacity_002_test')

    def test_filters_sepia_001_test(self):
        self.assertRender('test_Filters1', 'filters_sepia_001_test')

    def test_filters_test_brightness_001(self):
        self.assertRender('test_Filters1', 'filters_test_brightness_001')

    def test_filters_test_brightness_002(self):
        self.assertRender('test_Filters1', 'filters_test_brightness_002')

    def test_filters_test_brightness_003(self):
        self.assertRender('test_Filters1', 'filters_test_brightness_003')

    def test_svg_feflood_001(self):
        self.assertRender('test_Filters1', 'svg_feflood_001')

    def test_svg_feimage_001(self):
        self.assertRender('test_Filters1', 'svg_feimage_001')

    def test_svg_feoffset_001(self):
        self.assertRender('test_Filters1', 'svg_feoffset_001')

