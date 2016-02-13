from unittest import expectedFailure
from .. utils import CSSWGTestCase

class test_CssTransforms1(CSSWGTestCase):
    def test_2d_rotate_001(self):
        self.assertRender('test_CssTransforms1', '2d_rotate_001')

    def test_2d_rotate_js(self):
        self.assertRender('test_CssTransforms1', '2d_rotate_js')

    def test_animations_001(self):
        self.assertRender('test_CssTransforms1', 'animations_001')

    def test_backface_visibility_hidden_001(self):
        self.assertRender('test_CssTransforms1', 'backface_visibility_hidden_001')

    def test_canvas3d_001(self):
        self.assertRender('test_CssTransforms1', 'canvas3d_001')

    def test_canvas3d_002(self):
        self.assertRender('test_CssTransforms1', 'canvas3d_002')

    def test_css_rotate_2d_3d_001(self):
        self.assertRender('test_CssTransforms1', 'css_rotate_2d_3d_001')

    def test_css_scale_nested_001(self):
        self.assertRender('test_CssTransforms1', 'css_scale_nested_001')

    def test_css_skew_001(self):
        self.assertRender('test_CssTransforms1', 'css_skew_001')

    def test_css_skew_002(self):
        self.assertRender('test_CssTransforms1', 'css_skew_002')

    def test_css_transform_3d_rotate3d_x_negative(self):
        self.assertRender('test_CssTransforms1', 'css_transform_3d_rotate3d_x_negative')

    def test_css_transform_3d_rotate3d_x_positive(self):
        self.assertRender('test_CssTransforms1', 'css_transform_3d_rotate3d_x_positive')

    def test_css_transform_3d_rotate3d_y_negative(self):
        self.assertRender('test_CssTransforms1', 'css_transform_3d_rotate3d_y_negative')

    def test_css_transform_3d_rotate3d_y_positive(self):
        self.assertRender('test_CssTransforms1', 'css_transform_3d_rotate3d_y_positive')

    def test_css_transform_3d_rotate3d_z_negative(self):
        self.assertRender('test_CssTransforms1', 'css_transform_3d_rotate3d_z_negative')

    def test_css_transform_3d_rotate3d_z_positive(self):
        self.assertRender('test_CssTransforms1', 'css_transform_3d_rotate3d_z_positive')

    def test_css_transform_3d_rotatex_negative(self):
        self.assertRender('test_CssTransforms1', 'css_transform_3d_rotatex_negative')

    def test_css_transform_3d_rotatex_positive(self):
        self.assertRender('test_CssTransforms1', 'css_transform_3d_rotatex_positive')

    def test_css_transform_3d_rotatey_negative(self):
        self.assertRender('test_CssTransforms1', 'css_transform_3d_rotatey_negative')

    def test_css_transform_3d_rotatey_positive(self):
        self.assertRender('test_CssTransforms1', 'css_transform_3d_rotatey_positive')

    def test_css_transform_3d_rotatez_negative(self):
        self.assertRender('test_CssTransforms1', 'css_transform_3d_rotatez_negative')

    def test_css_transform_3d_rotatez_positive(self):
        self.assertRender('test_CssTransforms1', 'css_transform_3d_rotatez_positive')

    def test_css_transform_3d_transform_style(self):
        self.assertRender('test_CssTransforms1', 'css_transform_3d_transform_style')

    def test_css_transform_inherit_rotate(self):
        self.assertRender('test_CssTransforms1', 'css_transform_inherit_rotate')

    def test_css_transform_inherit_scale(self):
        self.assertRender('test_CssTransforms1', 'css_transform_inherit_scale')

    def test_css_transform_property_existence(self):
        self.assertRender('test_CssTransforms1', 'css_transform_property_existence')

    def test_css_transform_scale_001(self):
        self.assertRender('test_CssTransforms1', 'css_transform_scale_001')

    def test_css_transform_scale_002(self):
        self.assertRender('test_CssTransforms1', 'css_transform_scale_002')

    def test_css_transform_style_evaluation_validation(self):
        self.assertRender('test_CssTransforms1', 'css_transform_style_evaluation_validation')

    def test_css_transforms_3d_on_anonymous_block_001(self):
        self.assertRender('test_CssTransforms1', 'css_transforms_3d_on_anonymous_block_001')

    def test_css_transforms_transformlist(self):
        self.assertRender('test_CssTransforms1', 'css_transforms_transformlist')

    def test_css3_transform_perspective(self):
        self.assertRender('test_CssTransforms1', 'css3_transform_perspective')

    def test_css3_transform_rotatey(self):
        self.assertRender('test_CssTransforms1', 'css3_transform_rotatey')

    def test_css3_transform_scale_002(self):
        self.assertRender('test_CssTransforms1', 'css3_transform_scale_002')

    def test_css3_transform_scale(self):
        self.assertRender('test_CssTransforms1', 'css3_transform_scale')

    def test_iframe_001(self):
        self.assertRender('test_CssTransforms1', 'iframe_001')

    def test_perspective_containing_block_dynamic_1a(self):
        self.assertRender('test_CssTransforms1', 'perspective_containing_block_dynamic_1a')

    def test_perspective_containing_block_dynamic_1b(self):
        self.assertRender('test_CssTransforms1', 'perspective_containing_block_dynamic_1b')

    def test_perspective_origin_001(self):
        self.assertRender('test_CssTransforms1', 'perspective_origin_001')

    def test_perspective_origin_002(self):
        self.assertRender('test_CssTransforms1', 'perspective_origin_002')

    def test_perspective_origin_003(self):
        self.assertRender('test_CssTransforms1', 'perspective_origin_003')

    def test_perspective_origin_004(self):
        self.assertRender('test_CssTransforms1', 'perspective_origin_004')

    def test_perspective_origin_005(self):
        self.assertRender('test_CssTransforms1', 'perspective_origin_005')

    def test_perspective_origin_006(self):
        self.assertRender('test_CssTransforms1', 'perspective_origin_006')

    def test_perspective_origin_x(self):
        self.assertRender('test_CssTransforms1', 'perspective_origin_x')

    def test_perspective_origin_xy(self):
        self.assertRender('test_CssTransforms1', 'perspective_origin_xy')

    def test_perspective_translatez_0(self):
        self.assertRender('test_CssTransforms1', 'perspective_translatez_0')

    def test_perspective_translatez_negative(self):
        self.assertRender('test_CssTransforms1', 'perspective_translatez_negative')

    def test_perspective_translatez_positive(self):
        self.assertRender('test_CssTransforms1', 'perspective_translatez_positive')

    def test_regions_transforms_001(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_001')

    def test_regions_transforms_002(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_002')

    def test_regions_transforms_003(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_003')

    def test_regions_transforms_004(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_004')

    def test_regions_transforms_005(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_005')

    def test_regions_transforms_006(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_006')

    def test_regions_transforms_007(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_007')

    def test_regions_transforms_008(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_008')

    def test_regions_transforms_009(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_009')

    def test_regions_transforms_010(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_010')

    def test_regions_transforms_011(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_011')

    def test_regions_transforms_012(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_012')

    def test_regions_transforms_013(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_013')

    def test_regions_transforms_014(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_014')

    def test_regions_transforms_015(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_015')

    def test_regions_transforms_016(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_016')

    def test_regions_transforms_017(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_017')

    def test_regions_transforms_018(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_018')

    def test_regions_transforms_019(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_019')

    def test_regions_transforms_020(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_020')

    def test_regions_transforms_021(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_021')

    def test_regions_transforms_022(self):
        self.assertRender('test_CssTransforms1', 'regions_transforms_022')

    def test_rotate_180_degrees_001(self):
        self.assertRender('test_CssTransforms1', 'rotate_180_degrees_001')

    def test_rotate_270_degrees_001(self):
        self.assertRender('test_CssTransforms1', 'rotate_270_degrees_001')

    def test_rotate_90_degrees_001(self):
        self.assertRender('test_CssTransforms1', 'rotate_90_degrees_001')

    def test_rotate_45deg(self):
        self.assertRender('test_CssTransforms1', 'rotate_45deg')

    def test_rotate_x_45deg(self):
        self.assertRender('test_CssTransforms1', 'rotate_x_45deg')

    def test_rotate_y_45deg(self):
        self.assertRender('test_CssTransforms1', 'rotate_y_45deg')

    def test_rotatey(self):
        self.assertRender('test_CssTransforms1', 'rotatey')

    def test_scale_optional_second_001(self):
        self.assertRender('test_CssTransforms1', 'scale_optional_second_001')

    def test_scale_zero_001(self):
        self.assertRender('test_CssTransforms1', 'scale_zero_001')

    def test_scalex(self):
        self.assertRender('test_CssTransforms1', 'scalex')

    def test_scaley(self):
        self.assertRender('test_CssTransforms1', 'scaley')

    def test_skew_test1(self):
        self.assertRender('test_CssTransforms1', 'skew_test1')

    def test_svg_document_styles_001(self):
        self.assertRender('test_CssTransforms1', 'svg_document_styles_001')

    def test_svg_document_styles_002(self):
        self.assertRender('test_CssTransforms1', 'svg_document_styles_002')

    def test_svg_document_styles_003(self):
        self.assertRender('test_CssTransforms1', 'svg_document_styles_003')

    def test_svg_document_styles_004(self):
        self.assertRender('test_CssTransforms1', 'svg_document_styles_004')

    def test_svg_document_styles_005(self):
        self.assertRender('test_CssTransforms1', 'svg_document_styles_005')

    def test_svg_document_styles_006(self):
        self.assertRender('test_CssTransforms1', 'svg_document_styles_006')

    def test_svg_document_styles_007(self):
        self.assertRender('test_CssTransforms1', 'svg_document_styles_007')

    def test_svg_document_styles_008(self):
        self.assertRender('test_CssTransforms1', 'svg_document_styles_008')

    def test_svg_document_styles_009(self):
        self.assertRender('test_CssTransforms1', 'svg_document_styles_009')

    def test_svg_document_styles_010(self):
        self.assertRender('test_CssTransforms1', 'svg_document_styles_010')

    def test_svg_document_styles_011(self):
        self.assertRender('test_CssTransforms1', 'svg_document_styles_011')

    def test_svg_document_styles_012(self):
        self.assertRender('test_CssTransforms1', 'svg_document_styles_012')

    def test_svg_document_styles_013(self):
        self.assertRender('test_CssTransforms1', 'svg_document_styles_013')

    def test_svg_document_styles_014(self):
        self.assertRender('test_CssTransforms1', 'svg_document_styles_014')

    def test_svg_external_styles_001(self):
        self.assertRender('test_CssTransforms1', 'svg_external_styles_001')

    def test_svg_external_styles_002(self):
        self.assertRender('test_CssTransforms1', 'svg_external_styles_002')

    def test_svg_external_styles_003(self):
        self.assertRender('test_CssTransforms1', 'svg_external_styles_003')

    def test_svg_external_styles_004(self):
        self.assertRender('test_CssTransforms1', 'svg_external_styles_004')

    def test_svg_external_styles_005(self):
        self.assertRender('test_CssTransforms1', 'svg_external_styles_005')

    def test_svg_external_styles_006(self):
        self.assertRender('test_CssTransforms1', 'svg_external_styles_006')

    def test_svg_external_styles_007(self):
        self.assertRender('test_CssTransforms1', 'svg_external_styles_007')

    def test_svg_external_styles_008(self):
        self.assertRender('test_CssTransforms1', 'svg_external_styles_008')

    def test_svg_external_styles_009(self):
        self.assertRender('test_CssTransforms1', 'svg_external_styles_009')

    def test_svg_external_styles_010(self):
        self.assertRender('test_CssTransforms1', 'svg_external_styles_010')

    def test_svg_external_styles_011(self):
        self.assertRender('test_CssTransforms1', 'svg_external_styles_011')

    def test_svg_external_styles_012(self):
        self.assertRender('test_CssTransforms1', 'svg_external_styles_012')

    def test_svg_external_styles_013(self):
        self.assertRender('test_CssTransforms1', 'svg_external_styles_013')

    def test_svg_external_styles_014(self):
        self.assertRender('test_CssTransforms1', 'svg_external_styles_014')

    def test_svg_gradienttransform_001(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_001')

    def test_svg_gradienttransform_002(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_002')

    def test_svg_gradienttransform_003(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_003')

    def test_svg_gradienttransform_004(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_004')

    def test_svg_gradienttransform_005(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_005')

    def test_svg_gradienttransform_006(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_006')

    def test_svg_gradienttransform_007(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_007')

    def test_svg_gradienttransform_008(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_008')

    def test_svg_gradienttransform_009(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_009')

    def test_svg_gradienttransform_010(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_010')

    def test_svg_gradienttransform_011(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_011')

    def test_svg_gradienttransform_012(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_012')

    def test_svg_gradienttransform_013(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_013')

    def test_svg_gradienttransform_014(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_014')

    def test_svg_gradienttransform_015(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_015')

    def test_svg_gradienttransform_016(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_016')

    def test_svg_gradienttransform_017(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_017')

    def test_svg_gradienttransform_018(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_018')

    def test_svg_gradienttransform_019(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_019')

    def test_svg_gradienttransform_020(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_020')

    def test_svg_gradienttransform_021(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_021')

    def test_svg_gradienttransform_022(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_022')

    def test_svg_gradienttransform_023(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_023')

    def test_svg_gradienttransform_024(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_024')

    def test_svg_gradienttransform_025(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_025')

    def test_svg_gradienttransform_026(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_026')

    def test_svg_gradienttransform_027(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_027')

    def test_svg_gradienttransform_028(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_028')

    def test_svg_gradienttransform_029(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_029')

    def test_svg_gradienttransform_030(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_030')

    def test_svg_gradienttransform_031(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_031')

    def test_svg_gradienttransform_032(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_032')

    def test_svg_gradienttransform_033(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_033')

    def test_svg_gradienttransform_034(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_034')

    def test_svg_gradienttransform_035(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_035')

    def test_svg_gradienttransform_036(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_036')

    def test_svg_gradienttransform_037(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_037')

    def test_svg_gradienttransform_038(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_038')

    def test_svg_gradienttransform_039(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_039')

    def test_svg_gradienttransform_040(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_040')

    def test_svg_gradienttransform_041(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_041')

    def test_svg_gradienttransform_042(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_042')

    def test_svg_gradienttransform_043(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_043')

    def test_svg_gradienttransform_044(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_044')

    def test_svg_gradienttransform_045(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_045')

    def test_svg_gradienttransform_046(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_046')

    def test_svg_gradienttransform_047(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_047')

    def test_svg_gradienttransform_048(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_048')

    def test_svg_gradienttransform_049(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_049')

    def test_svg_gradienttransform_combination_001(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_combination_001')

    def test_svg_gradienttransform_combination_002(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_combination_002')

    def test_svg_gradienttransform_combination_003(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_combination_003')

    def test_svg_gradienttransform_ex_unit_001(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_ex_unit_001')

    def test_svg_gradienttransform_ex_unit_002(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_ex_unit_002')

    def test_svg_gradienttransform_ex_unit_003(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_ex_unit_003')

    def test_svg_gradienttransform_ex_unit_004(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_ex_unit_004')

    def test_svg_gradienttransform_ex_unit_005(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_ex_unit_005')

    def test_svg_gradienttransform_ex_unit_006(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_ex_unit_006')

    def test_svg_gradienttransform_relative_001(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_relative_001')

    def test_svg_gradienttransform_relative_002(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_relative_002')

    def test_svg_gradienttransform_relative_003(self):
        self.assertRender('test_CssTransforms1', 'svg_gradienttransform_relative_003')

    def test_svg_inline_styles_001(self):
        self.assertRender('test_CssTransforms1', 'svg_inline_styles_001')

    def test_svg_inline_styles_002(self):
        self.assertRender('test_CssTransforms1', 'svg_inline_styles_002')

    def test_svg_inline_styles_003(self):
        self.assertRender('test_CssTransforms1', 'svg_inline_styles_003')

    def test_svg_inline_styles_004(self):
        self.assertRender('test_CssTransforms1', 'svg_inline_styles_004')

    def test_svg_inline_styles_005(self):
        self.assertRender('test_CssTransforms1', 'svg_inline_styles_005')

    def test_svg_inline_styles_006(self):
        self.assertRender('test_CssTransforms1', 'svg_inline_styles_006')

    def test_svg_inline_styles_007(self):
        self.assertRender('test_CssTransforms1', 'svg_inline_styles_007')

    def test_svg_inline_styles_008(self):
        self.assertRender('test_CssTransforms1', 'svg_inline_styles_008')

    def test_svg_inline_styles_009(self):
        self.assertRender('test_CssTransforms1', 'svg_inline_styles_009')

    def test_svg_inline_styles_010(self):
        self.assertRender('test_CssTransforms1', 'svg_inline_styles_010')

    def test_svg_inline_styles_011(self):
        self.assertRender('test_CssTransforms1', 'svg_inline_styles_011')

    def test_svg_inline_styles_012(self):
        self.assertRender('test_CssTransforms1', 'svg_inline_styles_012')

    def test_svg_inline_styles_013(self):
        self.assertRender('test_CssTransforms1', 'svg_inline_styles_013')

    def test_svg_inline_styles_014(self):
        self.assertRender('test_CssTransforms1', 'svg_inline_styles_014')

    def test_svg_matrix_001(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_001')

    def test_svg_matrix_002(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_002')

    def test_svg_matrix_003(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_003')

    def test_svg_matrix_004(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_004')

    def test_svg_matrix_005(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_005')

    def test_svg_matrix_006(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_006')

    def test_svg_matrix_007(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_007')

    def test_svg_matrix_008(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_008')

    def test_svg_matrix_009(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_009')

    def test_svg_matrix_010(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_010')

    def test_svg_matrix_011(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_011')

    def test_svg_matrix_012(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_012')

    def test_svg_matrix_013(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_013')

    def test_svg_matrix_014(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_014')

    def test_svg_matrix_015(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_015')

    def test_svg_matrix_016(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_016')

    def test_svg_matrix_017(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_017')

    def test_svg_matrix_018(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_018')

    def test_svg_matrix_019(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_019')

    def test_svg_matrix_020(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_020')

    def test_svg_matrix_021(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_021')

    def test_svg_matrix_022(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_022')

    def test_svg_matrix_023(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_023')

    def test_svg_matrix_024(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_024')

    def test_svg_matrix_025(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_025')

    def test_svg_matrix_026(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_026')

    def test_svg_matrix_027(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_027')

    def test_svg_matrix_028(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_028')

    def test_svg_matrix_029(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_029')

    def test_svg_matrix_030(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_030')

    def test_svg_matrix_031(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_031')

    def test_svg_matrix_032(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_032')

    def test_svg_matrix_033(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_033')

    def test_svg_matrix_034(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_034')

    def test_svg_matrix_035(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_035')

    def test_svg_matrix_036(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_036')

    def test_svg_matrix_037(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_037')

    def test_svg_matrix_038(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_038')

    def test_svg_matrix_039(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_039')

    def test_svg_matrix_040(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_040')

    def test_svg_matrix_041(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_041')

    def test_svg_matrix_042(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_042')

    def test_svg_matrix_043(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_043')

    def test_svg_matrix_044(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_044')

    def test_svg_matrix_045(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_045')

    def test_svg_matrix_046(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_046')

    def test_svg_matrix_047(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_047')

    def test_svg_matrix_048(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_048')

    def test_svg_matrix_049(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_049')

    def test_svg_matrix_050(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_050')

    def test_svg_matrix_051(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_051')

    def test_svg_matrix_052(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_052')

    def test_svg_matrix_053(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_053')

    def test_svg_matrix_054(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_054')

    def test_svg_matrix_055(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_055')

    def test_svg_matrix_056(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_056')

    def test_svg_matrix_057(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_057')

    def test_svg_matrix_058(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_058')

    def test_svg_matrix_059(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_059')

    def test_svg_matrix_060(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_060')

    def test_svg_matrix_061(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_061')

    def test_svg_matrix_062(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_062')

    def test_svg_matrix_063(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_063')

    def test_svg_matrix_064(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_064')

    def test_svg_matrix_065(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_065')

    def test_svg_matrix_066(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_066')

    def test_svg_matrix_067(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_067')

    def test_svg_matrix_068(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_068')

    def test_svg_matrix_069(self):
        self.assertRender('test_CssTransforms1', 'svg_matrix_069')

    def test_svg_origin_length_001(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_001')

    def test_svg_origin_length_002(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_002')

    def test_svg_origin_length_003(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_003')

    def test_svg_origin_length_004(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_004')

    def test_svg_origin_length_005(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_005')

    def test_svg_origin_length_006(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_006')

    def test_svg_origin_length_007(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_007')

    def test_svg_origin_length_008(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_008')

    def test_svg_origin_length_cm_001(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_cm_001')

    def test_svg_origin_length_cm_002(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_cm_002')

    def test_svg_origin_length_cm_003(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_cm_003')

    def test_svg_origin_length_cm_004(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_cm_004')

    def test_svg_origin_length_cm_005(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_cm_005')

    def test_svg_origin_length_in_001(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_in_001')

    def test_svg_origin_length_in_002(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_in_002')

    def test_svg_origin_length_in_003(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_in_003')

    def test_svg_origin_length_in_004(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_in_004')

    def test_svg_origin_length_in_005(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_in_005')

    def test_svg_origin_length_pt_001(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_pt_001')

    def test_svg_origin_length_pt_002(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_pt_002')

    def test_svg_origin_length_pt_003(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_pt_003')

    def test_svg_origin_length_pt_004(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_pt_004')

    def test_svg_origin_length_pt_005(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_length_pt_005')

    def test_svg_origin_relative_length_001(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_001')

    def test_svg_origin_relative_length_002(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_002')

    def test_svg_origin_relative_length_003(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_003')

    def test_svg_origin_relative_length_004(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_004')

    def test_svg_origin_relative_length_005(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_005')

    def test_svg_origin_relative_length_006(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_006')

    def test_svg_origin_relative_length_007(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_007')

    def test_svg_origin_relative_length_008(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_008')

    def test_svg_origin_relative_length_009(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_009')

    def test_svg_origin_relative_length_010(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_010')

    def test_svg_origin_relative_length_011(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_011')

    def test_svg_origin_relative_length_012(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_012')

    def test_svg_origin_relative_length_013(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_013')

    def test_svg_origin_relative_length_014(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_014')

    def test_svg_origin_relative_length_015(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_015')

    def test_svg_origin_relative_length_016(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_016')

    def test_svg_origin_relative_length_017(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_017')

    def test_svg_origin_relative_length_018(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_018')

    def test_svg_origin_relative_length_019(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_019')

    def test_svg_origin_relative_length_020(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_020')

    def test_svg_origin_relative_length_021(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_021')

    def test_svg_origin_relative_length_022(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_022')

    def test_svg_origin_relative_length_023(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_023')

    def test_svg_origin_relative_length_024(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_024')

    def test_svg_origin_relative_length_025(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_025')

    def test_svg_origin_relative_length_026(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_026')

    def test_svg_origin_relative_length_027(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_027')

    def test_svg_origin_relative_length_028(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_028')

    def test_svg_origin_relative_length_029(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_029')

    def test_svg_origin_relative_length_030(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_030')

    def test_svg_origin_relative_length_031(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_031')

    def test_svg_origin_relative_length_032(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_032')

    def test_svg_origin_relative_length_033(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_033')

    def test_svg_origin_relative_length_034(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_034')

    def test_svg_origin_relative_length_035(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_035')

    def test_svg_origin_relative_length_036(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_036')

    def test_svg_origin_relative_length_037(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_037')

    def test_svg_origin_relative_length_038(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_038')

    def test_svg_origin_relative_length_039(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_039')

    def test_svg_origin_relative_length_040(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_040')

    def test_svg_origin_relative_length_041(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_041')

    def test_svg_origin_relative_length_042(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_042')

    def test_svg_origin_relative_length_043(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_043')

    def test_svg_origin_relative_length_044(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_044')

    def test_svg_origin_relative_length_045(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_045')

    def test_svg_origin_relative_length_046(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_046')

    def test_svg_origin_relative_length_invalid_001(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_invalid_001')

    def test_svg_origin_relative_length_invalid_002(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_invalid_002')

    def test_svg_origin_relative_length_invalid_003(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_invalid_003')

    def test_svg_origin_relative_length_invalid_004(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_invalid_004')

    def test_svg_origin_relative_length_invalid_005(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_invalid_005')

    def test_svg_origin_relative_length_invalid_006(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_invalid_006')

    def test_svg_origin_relative_length_invalid_007(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_invalid_007')

    def test_svg_origin_relative_length_invalid_008(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_invalid_008')

    def test_svg_origin_relative_length_invalid_009(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_invalid_009')

    def test_svg_origin_relative_length_invalid_010(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_invalid_010')

    def test_svg_origin_relative_length_invalid_011(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_invalid_011')

    def test_svg_origin_relative_length_invalid_012(self):
        self.assertRender('test_CssTransforms1', 'svg_origin_relative_length_invalid_012')

    def test_svg_patterntransform_001(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_001')

    def test_svg_patterntransform_002(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_002')

    def test_svg_patterntransform_003(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_003')

    def test_svg_patterntransform_004(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_004')

    def test_svg_patterntransform_005(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_005')

    def test_svg_patterntransform_006(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_006')

    def test_svg_patterntransform_007(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_007')

    def test_svg_patterntransform_008(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_008')

    def test_svg_patterntransform_009(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_009')

    def test_svg_patterntransform_010(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_010')

    def test_svg_patterntransform_011(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_011')

    def test_svg_patterntransform_012(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_012')

    def test_svg_patterntransform_013(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_013')

    def test_svg_patterntransform_014(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_014')

    def test_svg_patterntransform_015(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_015')

    def test_svg_patterntransform_016(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_016')

    def test_svg_patterntransform_017(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_017')

    def test_svg_patterntransform_018(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_018')

    def test_svg_patterntransform_019(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_019')

    def test_svg_patterntransform_020(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_020')

    def test_svg_patterntransform_021(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_021')

    def test_svg_patterntransform_022(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_022')

    def test_svg_patterntransform_023(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_023')

    def test_svg_patterntransform_024(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_024')

    def test_svg_patterntransform_025(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_025')

    def test_svg_patterntransform_026(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_026')

    def test_svg_patterntransform_027(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_027')

    def test_svg_patterntransform_028(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_028')

    def test_svg_patterntransform_029(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_029')

    def test_svg_patterntransform_030(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_030')

    def test_svg_patterntransform_031(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_031')

    def test_svg_patterntransform_032(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_032')

    def test_svg_patterntransform_033(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_033')

    def test_svg_patterntransform_034(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_034')

    def test_svg_patterntransform_035(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_035')

    def test_svg_patterntransform_036(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_036')

    def test_svg_patterntransform_037(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_037')

    def test_svg_patterntransform_038(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_038')

    def test_svg_patterntransform_039(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_039')

    def test_svg_patterntransform_040(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_040')

    def test_svg_patterntransform_041(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_041')

    def test_svg_patterntransform_042(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_042')

    def test_svg_patterntransform_043(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_043')

    def test_svg_patterntransform_044(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_044')

    def test_svg_patterntransform_045(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_045')

    def test_svg_patterntransform_046(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_046')

    def test_svg_patterntransform_047(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_047')

    def test_svg_patterntransform_048(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_048')

    def test_svg_patterntransform_049(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_049')

    def test_svg_patterntransform_combination_001(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_combination_001')

    def test_svg_patterntransform_combination_002(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_combination_002')

    def test_svg_patterntransform_combination_003(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_combination_003')

    def test_svg_patterntransform_ex_unit_001(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_ex_unit_001')

    def test_svg_patterntransform_ex_unit_002(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_ex_unit_002')

    def test_svg_patterntransform_ex_unit_003(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_ex_unit_003')

    def test_svg_patterntransform_ex_unit_004(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_ex_unit_004')

    def test_svg_patterntransform_ex_unit_005(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_ex_unit_005')

    def test_svg_patterntransform_ex_unit_006(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_ex_unit_006')

    def test_svg_patterntransform_relative_001(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_relative_001')

    def test_svg_patterntransform_relative_002(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_relative_002')

    def test_svg_patterntransform_relative_003(self):
        self.assertRender('test_CssTransforms1', 'svg_patterntransform_relative_003')

    def test_svg_rotate_3args_001(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_001')

    def test_svg_rotate_3args_002(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_002')

    def test_svg_rotate_3args_003(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_003')

    def test_svg_rotate_3args_004(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_004')

    def test_svg_rotate_3args_005(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_005')

    def test_svg_rotate_3args_006(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_006')

    def test_svg_rotate_3args_007(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_007')

    def test_svg_rotate_3args_008(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_008')

    def test_svg_rotate_3args_009(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_009')

    def test_svg_rotate_3args_010(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_010')

    def test_svg_rotate_3args_011(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_011')

    def test_svg_rotate_3args_012(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_012')

    def test_svg_rotate_3args_013(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_013')

    def test_svg_rotate_3args_014(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_014')

    def test_svg_rotate_3args_015(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_015')

    def test_svg_rotate_3args_016(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_016')

    def test_svg_rotate_3args_017(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_017')

    def test_svg_rotate_3args_018(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_018')

    def test_svg_rotate_3args_019(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_019')

    def test_svg_rotate_3args_020(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_020')

    def test_svg_rotate_3args_021(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_021')

    def test_svg_rotate_3args_022(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_022')

    def test_svg_rotate_3args_023(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_023')

    def test_svg_rotate_3args_invalid_001(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_invalid_001')

    def test_svg_rotate_3args_invalid_002(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_invalid_002')

    def test_svg_rotate_3args_invalid_003(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_invalid_003')

    def test_svg_rotate_3args_invalid_004(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_invalid_004')

    def test_svg_rotate_3args_invalid_005(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_3args_invalid_005')

    def test_svg_rotate_angle_45_001(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_001')

    def test_svg_rotate_angle_45_002(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_002')

    def test_svg_rotate_angle_45_003(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_003')

    def test_svg_rotate_angle_45_004(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_004')

    def test_svg_rotate_angle_45_005(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_005')

    def test_svg_rotate_angle_45_006(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_006')

    def test_svg_rotate_angle_45_007(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_007')

    def test_svg_rotate_angle_45_008(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_008')

    def test_svg_rotate_angle_45_009(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_009')

    def test_svg_rotate_angle_45_010(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_010')

    def test_svg_rotate_angle_45_011(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_011')

    def test_svg_rotate_angle_45_012(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_012')

    def test_svg_rotate_angle_45_013(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_013')

    def test_svg_rotate_angle_45_014(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_014')

    def test_svg_rotate_angle_45_015(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_015')

    def test_svg_rotate_angle_45_016(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_016')

    def test_svg_rotate_angle_45_017(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_017')

    def test_svg_rotate_angle_45_018(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_018')

    def test_svg_rotate_angle_45_019(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_019')

    def test_svg_rotate_angle_45_020(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_020')

    def test_svg_rotate_angle_45_021(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_021')

    def test_svg_rotate_angle_45_022(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_022')

    def test_svg_rotate_angle_45_023(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_023')

    def test_svg_rotate_angle_45_024(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_024')

    def test_svg_rotate_angle_45_025(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_45_025')

    def test_svg_rotate_angle_90_001(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_001')

    def test_svg_rotate_angle_90_002(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_002')

    def test_svg_rotate_angle_90_003(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_003')

    def test_svg_rotate_angle_90_004(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_004')

    def test_svg_rotate_angle_90_005(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_005')

    def test_svg_rotate_angle_90_006(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_006')

    def test_svg_rotate_angle_90_007(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_007')

    def test_svg_rotate_angle_90_008(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_008')

    def test_svg_rotate_angle_90_009(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_009')

    def test_svg_rotate_angle_90_010(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_010')

    def test_svg_rotate_angle_90_011(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_011')

    def test_svg_rotate_angle_90_012(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_012')

    def test_svg_rotate_angle_90_013(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_013')

    def test_svg_rotate_angle_90_014(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_014')

    def test_svg_rotate_angle_90_015(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_015')

    def test_svg_rotate_angle_90_016(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_016')

    def test_svg_rotate_angle_90_017(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_017')

    def test_svg_rotate_angle_90_018(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_018')

    def test_svg_rotate_angle_90_019(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_019')

    def test_svg_rotate_angle_90_020(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_020')

    def test_svg_rotate_angle_90_021(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_021')

    def test_svg_rotate_angle_90_022(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_022')

    def test_svg_rotate_angle_90_023(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_023')

    def test_svg_rotate_angle_90_024(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_024')

    def test_svg_rotate_angle_90_025(self):
        self.assertRender('test_CssTransforms1', 'svg_rotate_angle_90_025')

    def test_svg_scale_001(self):
        self.assertRender('test_CssTransforms1', 'svg_scale_001')

    def test_svg_scale_002(self):
        self.assertRender('test_CssTransforms1', 'svg_scale_002')

    def test_svg_scale_003(self):
        self.assertRender('test_CssTransforms1', 'svg_scale_003')

    def test_svg_scale_004(self):
        self.assertRender('test_CssTransforms1', 'svg_scale_004')

    def test_svg_scale_005(self):
        self.assertRender('test_CssTransforms1', 'svg_scale_005')

    def test_svg_scale_006(self):
        self.assertRender('test_CssTransforms1', 'svg_scale_006')

    def test_svg_scale_007(self):
        self.assertRender('test_CssTransforms1', 'svg_scale_007')

    def test_svg_scale_008(self):
        self.assertRender('test_CssTransforms1', 'svg_scale_008')

    def test_svg_scale_009(self):
        self.assertRender('test_CssTransforms1', 'svg_scale_009')

    def test_svg_scale_010(self):
        self.assertRender('test_CssTransforms1', 'svg_scale_010')

    def test_svg_scale_011(self):
        self.assertRender('test_CssTransforms1', 'svg_scale_011')

    def test_svg_scale_012(self):
        self.assertRender('test_CssTransforms1', 'svg_scale_012')

    def test_svg_scale_013(self):
        self.assertRender('test_CssTransforms1', 'svg_scale_013')

    def test_svg_scale_014(self):
        self.assertRender('test_CssTransforms1', 'svg_scale_014')

    def test_svg_scale_015(self):
        self.assertRender('test_CssTransforms1', 'svg_scale_015')

    def test_svg_scale_016(self):
        self.assertRender('test_CssTransforms1', 'svg_scale_016')

    def test_svg_scale_017(self):
        self.assertRender('test_CssTransforms1', 'svg_scale_017')

    def test_svg_scalex_001(self):
        self.assertRender('test_CssTransforms1', 'svg_scalex_001')

    def test_svg_scalex_002(self):
        self.assertRender('test_CssTransforms1', 'svg_scalex_002')

    def test_svg_scalex_003(self):
        self.assertRender('test_CssTransforms1', 'svg_scalex_003')

    def test_svg_scalex_004(self):
        self.assertRender('test_CssTransforms1', 'svg_scalex_004')

    def test_svg_scalex_005(self):
        self.assertRender('test_CssTransforms1', 'svg_scalex_005')

    def test_svg_scaley_001(self):
        self.assertRender('test_CssTransforms1', 'svg_scaley_001')

    def test_svg_scaley_002(self):
        self.assertRender('test_CssTransforms1', 'svg_scaley_002')

    def test_svg_scaley_003(self):
        self.assertRender('test_CssTransforms1', 'svg_scaley_003')

    def test_svg_scaley_004(self):
        self.assertRender('test_CssTransforms1', 'svg_scaley_004')

    def test_svg_scaley_005(self):
        self.assertRender('test_CssTransforms1', 'svg_scaley_005')

    def test_svg_skewx_001(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_001')

    def test_svg_skewx_002(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_002')

    def test_svg_skewx_003(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_003')

    def test_svg_skewx_004(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_004')

    def test_svg_skewx_005(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_005')

    def test_svg_skewx_006(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_006')

    def test_svg_skewx_007(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_007')

    def test_svg_skewx_008(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_008')

    def test_svg_skewx_009(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_009')

    def test_svg_skewx_010(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_010')

    def test_svg_skewx_011(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_011')

    def test_svg_skewx_012(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_012')

    def test_svg_skewx_013(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_013')

    def test_svg_skewx_014(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_014')

    def test_svg_skewx_015(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_015')

    def test_svg_skewx_016(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_016')

    def test_svg_skewx_017(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_017')

    def test_svg_skewx_018(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_018')

    def test_svg_skewx_019(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_019')

    def test_svg_skewx_020(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_020')

    def test_svg_skewx_021(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_021')

    def test_svg_skewx_022(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_022')

    def test_svg_skewx_023(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_023')

    def test_svg_skewx_024(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_024')

    def test_svg_skewx_025(self):
        self.assertRender('test_CssTransforms1', 'svg_skewx_025')

    def test_svg_skewxy_001(self):
        self.assertRender('test_CssTransforms1', 'svg_skewxy_001')

    def test_svg_skewxy_002(self):
        self.assertRender('test_CssTransforms1', 'svg_skewxy_002')

    def test_svg_skewy_001(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_001')

    def test_svg_skewy_002(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_002')

    def test_svg_skewy_003(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_003')

    def test_svg_skewy_004(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_004')

    def test_svg_skewy_005(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_005')

    def test_svg_skewy_006(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_006')

    def test_svg_skewy_007(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_007')

    def test_svg_skewy_008(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_008')

    def test_svg_skewy_009(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_009')

    def test_svg_skewy_010(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_010')

    def test_svg_skewy_011(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_011')

    def test_svg_skewy_012(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_012')

    def test_svg_skewy_013(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_013')

    def test_svg_skewy_014(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_014')

    def test_svg_skewy_015(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_015')

    def test_svg_skewy_016(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_016')

    def test_svg_skewy_017(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_017')

    def test_svg_skewy_018(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_018')

    def test_svg_skewy_019(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_019')

    def test_svg_skewy_020(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_020')

    def test_svg_skewy_021(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_021')

    def test_svg_skewy_022(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_022')

    def test_svg_skewy_023(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_023')

    def test_svg_skewy_024(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_024')

    def test_svg_skewy_025(self):
        self.assertRender('test_CssTransforms1', 'svg_skewy_025')

    def test_svg_transform_group_001(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_group_001')

    def test_svg_transform_group_002(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_group_002')

    def test_svg_transform_group_003(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_group_003')

    def test_svg_transform_group_004(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_group_004')

    def test_svg_transform_group_005(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_group_005')

    def test_svg_transform_group_006(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_group_006')

    def test_svg_transform_group_007(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_group_007')

    def test_svg_transform_group_008(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_group_008')

    def test_svg_transform_group_009(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_group_009')

    def test_svg_transform_group_010(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_group_010')

    def test_svg_transform_group_011(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_group_011')

    def test_svg_transform_list_separations_001(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_list_separations_001')

    def test_svg_transform_list_separations_002(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_list_separations_002')

    def test_svg_transform_list_separations_003(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_list_separations_003')

    def test_svg_transform_list_separations_004(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_list_separations_004')

    def test_svg_transform_list_separations_005(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_list_separations_005')

    def test_svg_transform_list_separations_006(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_list_separations_006')

    def test_svg_transform_list_separations_007(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_list_separations_007')

    def test_svg_transform_list_separations_008(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_list_separations_008')

    def test_svg_transform_list_separations_009(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_list_separations_009')

    def test_svg_transform_list_separations_010(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_list_separations_010')

    def test_svg_transform_list_separations_011(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_list_separations_011')

    def test_svg_transform_nested_001(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_001')

    def test_svg_transform_nested_002(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_002')

    def test_svg_transform_nested_003(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_003')

    def test_svg_transform_nested_004(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_004')

    def test_svg_transform_nested_005(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_005')

    def test_svg_transform_nested_006(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_006')

    def test_svg_transform_nested_007(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_007')

    def test_svg_transform_nested_008(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_008')

    def test_svg_transform_nested_009(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_009')

    def test_svg_transform_nested_010(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_010')

    def test_svg_transform_nested_011(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_011')

    def test_svg_transform_nested_012(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_012')

    def test_svg_transform_nested_013(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_013')

    def test_svg_transform_nested_014(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_014')

    def test_svg_transform_nested_015(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_015')

    def test_svg_transform_nested_016(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_016')

    def test_svg_transform_nested_017(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_017')

    def test_svg_transform_nested_018(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_018')

    def test_svg_transform_nested_019(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_019')

    def test_svg_transform_nested_020(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_020')

    def test_svg_transform_nested_021(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_021')

    def test_svg_transform_nested_022(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_022')

    def test_svg_transform_nested_023(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_023')

    def test_svg_transform_nested_024(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_024')

    def test_svg_transform_nested_025(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_025')

    def test_svg_transform_nested_026(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_026')

    def test_svg_transform_nested_027(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_027')

    def test_svg_transform_nested_028(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_028')

    def test_svg_transform_nested_029(self):
        self.assertRender('test_CssTransforms1', 'svg_transform_nested_029')

    def test_svg_translate_001(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_001')

    def test_svg_translate_002(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_002')

    def test_svg_translate_003(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_003')

    def test_svg_translate_004(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_004')

    def test_svg_translate_005(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_005')

    def test_svg_translate_006(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_006')

    def test_svg_translate_007(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_007')

    def test_svg_translate_008(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_008')

    def test_svg_translate_009(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_009')

    def test_svg_translate_010(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_010')

    def test_svg_translate_011(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_011')

    def test_svg_translate_012(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_012')

    def test_svg_translate_013(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_013')

    def test_svg_translate_014(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_014')

    def test_svg_translate_015(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_015')

    def test_svg_translate_016(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_016')

    def test_svg_translate_017(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_017')

    def test_svg_translate_018(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_018')

    def test_svg_translate_019(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_019')

    def test_svg_translate_020(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_020')

    def test_svg_translate_021(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_021')

    def test_svg_translate_022(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_022')

    def test_svg_translate_023(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_023')

    def test_svg_translate_024(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_024')

    def test_svg_translate_025(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_025')

    def test_svg_translate_026(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_026')

    def test_svg_translate_027(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_027')

    def test_svg_translate_028(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_028')

    def test_svg_translate_029(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_029')

    def test_svg_translate_030(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_030')

    def test_svg_translate_031(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_031')

    def test_svg_translate_032(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_032')

    def test_svg_translate_033(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_033')

    def test_svg_translate_034(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_034')

    def test_svg_translate_035(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_035')

    def test_svg_translate_036(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_036')

    def test_svg_translate_037(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_037')

    def test_svg_translate_038(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_038')

    def test_svg_translate_039(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_039')

    def test_svg_translate_040(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_040')

    def test_svg_translate_041(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_041')

    def test_svg_translate_042(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_042')

    def test_svg_translate_043(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_043')

    def test_svg_translate_044(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_044')

    def test_svg_translate_045(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_045')

    def test_svg_translate_046(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_046')

    def test_svg_translate_047(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_047')

    def test_svg_translate_048(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_048')

    def test_svg_translate_049(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_049')

    def test_svg_translate_050(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_050')

    def test_svg_translate_051(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_051')

    def test_svg_translate_052(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_052')

    def test_svg_translate_053(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_053')

    def test_svg_translate_054(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_054')

    def test_svg_translate_055(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_055')

    def test_svg_translate_abs_unit_combinations_001(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_abs_unit_combinations_001')

    def test_svg_translate_abs_unit_combinations_002(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_abs_unit_combinations_002')

    def test_svg_translate_abs_unit_combinations_003(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_abs_unit_combinations_003')

    def test_svg_translate_abs_unit_combinations_004(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_abs_unit_combinations_004')

    def test_svg_translate_abs_unit_combinations_005(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_abs_unit_combinations_005')

    def test_svg_translate_abs_unit_combinations_006(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_abs_unit_combinations_006')

    def test_svg_translate_ex_unit_001(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_ex_unit_001')

    def test_svg_translate_ex_unit_002(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_ex_unit_002')

    def test_svg_translate_ex_unit_003(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_ex_unit_003')

    def test_svg_translate_ex_unit_004(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_ex_unit_004')

    def test_svg_translate_ex_unit_005(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_ex_unit_005')

    def test_svg_translate_ex_unit_006(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_ex_unit_006')

    def test_svg_translate_multiple_001(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_multiple_001')

    def test_svg_translate_multiple_002(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_multiple_002')

    def test_svg_translate_multiple_relative_001(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_multiple_relative_001')

    def test_svg_translate_multiple_relative_002(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_multiple_relative_002')

    def test_svg_translate_relative_001(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_relative_001')

    def test_svg_translate_relative_002(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_relative_002')

    def test_svg_translate_relative_003(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_relative_003')

    def test_svg_translate_relative_004(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_relative_004')

    def test_svg_translate_relative_005(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_relative_005')

    def test_svg_translate_relative_006(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_relative_006')

    def test_svg_translate_relative_007(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_relative_007')

    def test_svg_translate_relative_008(self):
        self.assertRender('test_CssTransforms1', 'svg_translate_relative_008')

    def test_svg_translatex_001(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_001')

    def test_svg_translatex_002(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_002')

    def test_svg_translatex_003(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_003')

    def test_svg_translatex_004(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_004')

    def test_svg_translatex_005(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_005')

    def test_svg_translatex_006(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_006')

    def test_svg_translatex_007(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_007')

    def test_svg_translatex_008(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_008')

    def test_svg_translatex_009(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_009')

    def test_svg_translatex_010(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_010')

    def test_svg_translatex_011(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_011')

    def test_svg_translatex_012(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_012')

    def test_svg_translatex_013(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_013')

    def test_svg_translatex_014(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_014')

    def test_svg_translatex_015(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_015')

    def test_svg_translatex_016(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_016')

    def test_svg_translatex_017(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_017')

    def test_svg_translatex_018(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_018')

    def test_svg_translatex_019(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_019')

    def test_svg_translatex_020(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_020')

    def test_svg_translatex_021(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_021')

    def test_svg_translatex_022(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_022')

    def test_svg_translatex_023(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_023')

    def test_svg_translatex_024(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_024')

    def test_svg_translatex_025(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_025')

    def test_svg_translatex_026(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_026')

    def test_svg_translatex_027(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_027')

    def test_svg_translatex_028(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_028')

    def test_svg_translatex_029(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_029')

    def test_svg_translatex_030(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_030')

    def test_svg_translatex_031(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_031')

    def test_svg_translatex_032(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_032')

    def test_svg_translatex_033(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_033')

    def test_svg_translatex_034(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_034')

    def test_svg_translatex_035(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_035')

    def test_svg_translatex_036(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_036')

    def test_svg_translatex_037(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_037')

    def test_svg_translatex_038(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_038')

    def test_svg_translatex_039(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_039')

    def test_svg_translatex_040(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_040')

    def test_svg_translatex_041(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_041')

    def test_svg_translatex_042(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_042')

    def test_svg_translatex_043(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_043')

    def test_svg_translatex_044(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_044')

    def test_svg_translatex_045(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_045')

    def test_svg_translatex_046(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_046')

    def test_svg_translatex_047(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_047')

    def test_svg_translatex_048(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_048')

    def test_svg_translatex_combination_001(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_combination_001')

    def test_svg_translatex_combination_002(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_combination_002')

    def test_svg_translatex_combination_003(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_combination_003')

    def test_svg_translatex_combination_004(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_combination_004')

    def test_svg_translatex_ex_unit_001(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_ex_unit_001')

    def test_svg_translatex_ex_unit_002(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_ex_unit_002')

    def test_svg_translatex_ex_unit_003(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_ex_unit_003')

    def test_svg_translatex_ex_unit_004(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_ex_unit_004')

    def test_svg_translatex_ex_unit_005(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_ex_unit_005')

    def test_svg_translatex_ex_unit_006(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_ex_unit_006')

    def test_svg_translatex_relative_001(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_relative_001')

    def test_svg_translatex_relative_002(self):
        self.assertRender('test_CssTransforms1', 'svg_translatex_relative_002')

    def test_svg_translatey_001(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_001')

    def test_svg_translatey_002(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_002')

    def test_svg_translatey_003(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_003')

    def test_svg_translatey_004(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_004')

    def test_svg_translatey_005(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_005')

    def test_svg_translatey_006(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_006')

    def test_svg_translatey_007(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_007')

    def test_svg_translatey_008(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_008')

    def test_svg_translatey_009(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_009')

    def test_svg_translatey_010(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_010')

    def test_svg_translatey_011(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_011')

    def test_svg_translatey_012(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_012')

    def test_svg_translatey_013(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_013')

    def test_svg_translatey_014(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_014')

    def test_svg_translatey_015(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_015')

    def test_svg_translatey_016(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_016')

    def test_svg_translatey_017(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_017')

    def test_svg_translatey_018(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_018')

    def test_svg_translatey_019(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_019')

    def test_svg_translatey_020(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_020')

    def test_svg_translatey_021(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_021')

    def test_svg_translatey_022(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_022')

    def test_svg_translatey_023(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_023')

    def test_svg_translatey_024(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_024')

    def test_svg_translatey_025(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_025')

    def test_svg_translatey_026(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_026')

    def test_svg_translatey_027(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_027')

    def test_svg_translatey_028(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_028')

    def test_svg_translatey_029(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_029')

    def test_svg_translatey_030(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_030')

    def test_svg_translatey_031(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_031')

    def test_svg_translatey_032(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_032')

    def test_svg_translatey_033(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_033')

    def test_svg_translatey_034(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_034')

    def test_svg_translatey_035(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_035')

    def test_svg_translatey_036(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_036')

    def test_svg_translatey_037(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_037')

    def test_svg_translatey_038(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_038')

    def test_svg_translatey_039(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_039')

    def test_svg_translatey_040(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_040')

    def test_svg_translatey_041(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_041')

    def test_svg_translatey_042(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_042')

    def test_svg_translatey_043(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_043')

    def test_svg_translatey_044(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_044')

    def test_svg_translatey_045(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_045')

    def test_svg_translatey_046(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_046')

    def test_svg_translatey_047(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_047')

    def test_svg_translatey_048(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_048')

    def test_svg_translatey_combination_001(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_combination_001')

    def test_svg_translatey_combination_002(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_combination_002')

    def test_svg_translatey_combination_003(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_combination_003')

    def test_svg_translatey_combination_004(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_combination_004')

    def test_svg_translatey_ex_unit_001(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_ex_unit_001')

    def test_svg_translatey_ex_unit_002(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_ex_unit_002')

    def test_svg_translatey_ex_unit_003(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_ex_unit_003')

    def test_svg_translatey_ex_unit_004(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_ex_unit_004')

    def test_svg_translatey_ex_unit_005(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_ex_unit_005')

    def test_svg_translatey_ex_unit_006(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_ex_unit_006')

    def test_svg_translatey_relative_001(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_relative_001')

    def test_svg_translatey_relative_002(self):
        self.assertRender('test_CssTransforms1', 'svg_translatey_relative_002')

    def test_transform_2d_getcomputedstyle_001(self):
        self.assertRender('test_CssTransforms1', 'transform_2d_getcomputedstyle_001')

    def test_transform_3d_rotatey_stair_above_001(self):
        self.assertRender('test_CssTransforms1', 'transform_3d_rotatey_stair_above_001')

    def test_transform_3d_rotatey_stair_below_001(self):
        self.assertRender('test_CssTransforms1', 'transform_3d_rotatey_stair_below_001')

    def test_transform_abspos_001(self):
        self.assertRender('test_CssTransforms1', 'transform_abspos_001')

    def test_transform_abspos_002(self):
        self.assertRender('test_CssTransforms1', 'transform_abspos_002')

    def test_transform_abspos_003(self):
        self.assertRender('test_CssTransforms1', 'transform_abspos_003')

    def test_transform_abspos_004(self):
        self.assertRender('test_CssTransforms1', 'transform_abspos_004')

    def test_transform_abspos_005(self):
        self.assertRender('test_CssTransforms1', 'transform_abspos_005')

    def test_transform_abspos_006(self):
        self.assertRender('test_CssTransforms1', 'transform_abspos_006')

    def test_transform_abspos_007(self):
        self.assertRender('test_CssTransforms1', 'transform_abspos_007')

    def test_transform_applies_to_001(self):
        self.assertRender('test_CssTransforms1', 'transform_applies_to_001')

    def test_transform_applies_to_002(self):
        self.assertRender('test_CssTransforms1', 'transform_applies_to_002')

    def test_transform_background_001(self):
        self.assertRender('test_CssTransforms1', 'transform_background_001')

    def test_transform_background_002(self):
        self.assertRender('test_CssTransforms1', 'transform_background_002')

    def test_transform_background_003(self):
        self.assertRender('test_CssTransforms1', 'transform_background_003')

    def test_transform_background_004(self):
        self.assertRender('test_CssTransforms1', 'transform_background_004')

    def test_transform_background_005(self):
        self.assertRender('test_CssTransforms1', 'transform_background_005')

    def test_transform_background_006(self):
        self.assertRender('test_CssTransforms1', 'transform_background_006')

    def test_transform_background_007(self):
        self.assertRender('test_CssTransforms1', 'transform_background_007')

    def test_transform_background_008(self):
        self.assertRender('test_CssTransforms1', 'transform_background_008')

    def test_transform_compound_001(self):
        self.assertRender('test_CssTransforms1', 'transform_compound_001')

    def test_transform_containing_block_dynamic_1a(self):
        self.assertRender('test_CssTransforms1', 'transform_containing_block_dynamic_1a')

    def test_transform_containing_block_dynamic_1b(self):
        self.assertRender('test_CssTransforms1', 'transform_containing_block_dynamic_1b')

    def test_transform_descendant_001(self):
        self.assertRender('test_CssTransforms1', 'transform_descendant_001')

    def test_transform_display_001(self):
        self.assertRender('test_CssTransforms1', 'transform_display_001')

    def test_transform_display_002(self):
        self.assertRender('test_CssTransforms1', 'transform_display_002')

    def test_transform_display_003(self):
        self.assertRender('test_CssTransforms1', 'transform_display_003')

    def test_transform_display_004(self):
        self.assertRender('test_CssTransforms1', 'transform_display_004')

    def test_transform_fixed_bg_001(self):
        self.assertRender('test_CssTransforms1', 'transform_fixed_bg_001')

    def test_transform_fixed_bg_002(self):
        self.assertRender('test_CssTransforms1', 'transform_fixed_bg_002')

    def test_transform_fixed_bg_003(self):
        self.assertRender('test_CssTransforms1', 'transform_fixed_bg_003')

    def test_transform_fixed_bg_004(self):
        self.assertRender('test_CssTransforms1', 'transform_fixed_bg_004')

    def test_transform_fixed_bg_005(self):
        self.assertRender('test_CssTransforms1', 'transform_fixed_bg_005')

    def test_transform_fixed_bg_006(self):
        self.assertRender('test_CssTransforms1', 'transform_fixed_bg_006')

    def test_transform_fixed_bg_007(self):
        self.assertRender('test_CssTransforms1', 'transform_fixed_bg_007')

    def test_transform_generated_001(self):
        self.assertRender('test_CssTransforms1', 'transform_generated_001')

    def test_transform_generated_002(self):
        self.assertRender('test_CssTransforms1', 'transform_generated_002')

    def test_transform_iframe_001(self):
        self.assertRender('test_CssTransforms1', 'transform_iframe_001')

    def test_transform_image_001(self):
        self.assertRender('test_CssTransforms1', 'transform_image_001')

    def test_transform_inherit_001(self):
        self.assertRender('test_CssTransforms1', 'transform_inherit_001')

    def test_transform_inherit_002(self):
        self.assertRender('test_CssTransforms1', 'transform_inherit_002')

    def test_transform_inherit_origin_001(self):
        self.assertRender('test_CssTransforms1', 'transform_inherit_origin_001')

    def test_transform_inherit_origin_002(self):
        self.assertRender('test_CssTransforms1', 'transform_inherit_origin_002')

    def test_transform_inline_001(self):
        self.assertRender('test_CssTransforms1', 'transform_inline_001')

    def test_transform_input_001(self):
        self.assertRender('test_CssTransforms1', 'transform_input_001')

    def test_transform_input_002(self):
        self.assertRender('test_CssTransforms1', 'transform_input_002')

    def test_transform_input_003(self):
        self.assertRender('test_CssTransforms1', 'transform_input_003')

    def test_transform_input_004(self):
        self.assertRender('test_CssTransforms1', 'transform_input_004')

    def test_transform_input_005(self):
        self.assertRender('test_CssTransforms1', 'transform_input_005')

    def test_transform_input_006(self):
        self.assertRender('test_CssTransforms1', 'transform_input_006')

    def test_transform_input_007(self):
        self.assertRender('test_CssTransforms1', 'transform_input_007')

    def test_transform_input_008(self):
        self.assertRender('test_CssTransforms1', 'transform_input_008')

    def test_transform_input_009(self):
        self.assertRender('test_CssTransforms1', 'transform_input_009')

    def test_transform_input_010(self):
        self.assertRender('test_CssTransforms1', 'transform_input_010')

    def test_transform_input_011(self):
        self.assertRender('test_CssTransforms1', 'transform_input_011')

    def test_transform_input_012(self):
        self.assertRender('test_CssTransforms1', 'transform_input_012')

    def test_transform_input_013(self):
        self.assertRender('test_CssTransforms1', 'transform_input_013')

    def test_transform_input_014(self):
        self.assertRender('test_CssTransforms1', 'transform_input_014')

    def test_transform_input_015(self):
        self.assertRender('test_CssTransforms1', 'transform_input_015')

    def test_transform_input_016(self):
        self.assertRender('test_CssTransforms1', 'transform_input_016')

    def test_transform_input_017(self):
        self.assertRender('test_CssTransforms1', 'transform_input_017')

    def test_transform_input_018(self):
        self.assertRender('test_CssTransforms1', 'transform_input_018')

    def test_transform_input_019(self):
        self.assertRender('test_CssTransforms1', 'transform_input_019')

    def test_transform_matrix_001(self):
        self.assertRender('test_CssTransforms1', 'transform_matrix_001')

    def test_transform_matrix_002(self):
        self.assertRender('test_CssTransforms1', 'transform_matrix_002')

    def test_transform_matrix_003(self):
        self.assertRender('test_CssTransforms1', 'transform_matrix_003')

    def test_transform_matrix_004(self):
        self.assertRender('test_CssTransforms1', 'transform_matrix_004')

    def test_transform_matrix_005(self):
        self.assertRender('test_CssTransforms1', 'transform_matrix_005')

    def test_transform_matrix_006(self):
        self.assertRender('test_CssTransforms1', 'transform_matrix_006')

    def test_transform_matrix_007(self):
        self.assertRender('test_CssTransforms1', 'transform_matrix_007')

    def test_transform_matrix_008(self):
        self.assertRender('test_CssTransforms1', 'transform_matrix_008')

    def test_transform_origin_001(self):
        self.assertRender('test_CssTransforms1', 'transform_origin_001')

    def test_transform_origin_002(self):
        self.assertRender('test_CssTransforms1', 'transform_origin_002')

    def test_transform_origin_003(self):
        self.assertRender('test_CssTransforms1', 'transform_origin_003')

    def test_transform_origin_004(self):
        self.assertRender('test_CssTransforms1', 'transform_origin_004')

    def test_transform_origin_005(self):
        self.assertRender('test_CssTransforms1', 'transform_origin_005')

    def test_transform_origin_006(self):
        self.assertRender('test_CssTransforms1', 'transform_origin_006')

    def test_transform_origin_007(self):
        self.assertRender('test_CssTransforms1', 'transform_origin_007')

    def test_transform_origin_008(self):
        self.assertRender('test_CssTransforms1', 'transform_origin_008')

    def test_transform_origin_009(self):
        self.assertRender('test_CssTransforms1', 'transform_origin_009')

    def test_transform_origin_01(self):
        self.assertRender('test_CssTransforms1', 'transform_origin_01')

    def test_transform_origin_010(self):
        self.assertRender('test_CssTransforms1', 'transform_origin_010')

    def test_transform_origin_011(self):
        self.assertRender('test_CssTransforms1', 'transform_origin_011')

    def test_transform_origin_012(self):
        self.assertRender('test_CssTransforms1', 'transform_origin_012')

    def test_transform_origin_name_001(self):
        self.assertRender('test_CssTransforms1', 'transform_origin_name_001')

    def test_transform_origin_name_002(self):
        self.assertRender('test_CssTransforms1', 'transform_origin_name_002')

    def test_transform_origin_name_003(self):
        self.assertRender('test_CssTransforms1', 'transform_origin_name_003')

    def test_transform_origin_name_004(self):
        self.assertRender('test_CssTransforms1', 'transform_origin_name_004')

    def test_transform_origin_name_005(self):
        self.assertRender('test_CssTransforms1', 'transform_origin_name_005')

    def test_transform_origin_name_006(self):
        self.assertRender('test_CssTransforms1', 'transform_origin_name_006')

    def test_transform_origin_name_007(self):
        self.assertRender('test_CssTransforms1', 'transform_origin_name_007')

    def test_transform_origin(self):
        self.assertRender('test_CssTransforms1', 'transform_origin')

    def test_transform_overflow_001(self):
        self.assertRender('test_CssTransforms1', 'transform_overflow_001')

    def test_transform_overflow_002(self):
        self.assertRender('test_CssTransforms1', 'transform_overflow_002')

    def test_transform_percent_001(self):
        self.assertRender('test_CssTransforms1', 'transform_percent_001')

    def test_transform_percent_002(self):
        self.assertRender('test_CssTransforms1', 'transform_percent_002')

    def test_transform_percent_003(self):
        self.assertRender('test_CssTransforms1', 'transform_percent_003')

    def test_transform_percent_004(self):
        self.assertRender('test_CssTransforms1', 'transform_percent_004')

    def test_transform_percent_005(self):
        self.assertRender('test_CssTransforms1', 'transform_percent_005')

    def test_transform_percent_006(self):
        self.assertRender('test_CssTransforms1', 'transform_percent_006')

    def test_transform_percent_007(self):
        self.assertRender('test_CssTransforms1', 'transform_percent_007')

    def test_transform_percent_008(self):
        self.assertRender('test_CssTransforms1', 'transform_percent_008')

    def test_transform_propagate_inherit_boolean_001(self):
        self.assertRender('test_CssTransforms1', 'transform_propagate_inherit_boolean_001')

    def test_transform_root_bg_001(self):
        self.assertRender('test_CssTransforms1', 'transform_root_bg_001')

    def test_transform_root_bg_002(self):
        self.assertRender('test_CssTransforms1', 'transform_root_bg_002')

    def test_transform_root_bg_003(self):
        self.assertRender('test_CssTransforms1', 'transform_root_bg_003')

    def test_transform_root_bg_004(self):
        self.assertRender('test_CssTransforms1', 'transform_root_bg_004')

    def test_transform_rotate_001(self):
        self.assertRender('test_CssTransforms1', 'transform_rotate_001')

    def test_transform_rotate_002(self):
        self.assertRender('test_CssTransforms1', 'transform_rotate_002')

    def test_transform_rotate_003(self):
        self.assertRender('test_CssTransforms1', 'transform_rotate_003')

    def test_transform_rotate_004(self):
        self.assertRender('test_CssTransforms1', 'transform_rotate_004')

    def test_transform_rotate_005(self):
        self.assertRender('test_CssTransforms1', 'transform_rotate_005')

    def test_transform_rotate_006(self):
        self.assertRender('test_CssTransforms1', 'transform_rotate_006')

    def test_transform_rotate_007(self):
        self.assertRender('test_CssTransforms1', 'transform_rotate_007')

    def test_transform_rounding_001(self):
        self.assertRender('test_CssTransforms1', 'transform_rounding_001')

    def test_transform_scale_001(self):
        self.assertRender('test_CssTransforms1', 'transform_scale_001')

    def test_transform_scale_002(self):
        self.assertRender('test_CssTransforms1', 'transform_scale_002')

    def test_transform_scale_percent_001(self):
        self.assertRender('test_CssTransforms1', 'transform_scale_percent_001')

    def test_transform_scale_test(self):
        self.assertRender('test_CssTransforms1', 'transform_scale_test')

    def test_transform_scalex_001(self):
        self.assertRender('test_CssTransforms1', 'transform_scalex_001')

    def test_transform_scaley_001(self):
        self.assertRender('test_CssTransforms1', 'transform_scaley_001')

    def test_transform_singular_001(self):
        self.assertRender('test_CssTransforms1', 'transform_singular_001')

    def test_transform_stacking_001(self):
        self.assertRender('test_CssTransforms1', 'transform_stacking_001')

    def test_transform_stacking_002(self):
        self.assertRender('test_CssTransforms1', 'transform_stacking_002')

    def test_transform_stacking_003(self):
        self.assertRender('test_CssTransforms1', 'transform_stacking_003')

    def test_transform_stacking_004(self):
        self.assertRender('test_CssTransforms1', 'transform_stacking_004')

    def test_transform_stresstest_001(self):
        self.assertRender('test_CssTransforms1', 'transform_stresstest_001')

    def test_transform_table_001(self):
        self.assertRender('test_CssTransforms1', 'transform_table_001')

    def test_transform_table_002(self):
        self.assertRender('test_CssTransforms1', 'transform_table_002')

    def test_transform_table_003(self):
        self.assertRender('test_CssTransforms1', 'transform_table_003')

    def test_transform_table_004(self):
        self.assertRender('test_CssTransforms1', 'transform_table_004')

    def test_transform_table_005(self):
        self.assertRender('test_CssTransforms1', 'transform_table_005')

    def test_transform_table_006(self):
        self.assertRender('test_CssTransforms1', 'transform_table_006')

    def test_transform_table_007(self):
        self.assertRender('test_CssTransforms1', 'transform_table_007')

    def test_transform_table_008(self):
        self.assertRender('test_CssTransforms1', 'transform_table_008')

    def test_transform_table_009(self):
        self.assertRender('test_CssTransforms1', 'transform_table_009')

    def test_transform_table_010(self):
        self.assertRender('test_CssTransforms1', 'transform_table_010')

    def test_transform_table_011(self):
        self.assertRender('test_CssTransforms1', 'transform_table_011')

    def test_transform_transformable_inline_block(self):
        self.assertRender('test_CssTransforms1', 'transform_transformable_inline_block')

    def test_transform_transformable_inline_table(self):
        self.assertRender('test_CssTransforms1', 'transform_transformable_inline_table')

    def test_transform_transformable_list_item(self):
        self.assertRender('test_CssTransforms1', 'transform_transformable_list_item')

    def test_transform_transformable_table_caption(self):
        self.assertRender('test_CssTransforms1', 'transform_transformable_table_caption')

    def test_transform_transformable_table_cell(self):
        self.assertRender('test_CssTransforms1', 'transform_transformable_table_cell')

    def test_transform_transformable_table_footer_group(self):
        self.assertRender('test_CssTransforms1', 'transform_transformable_table_footer_group')

    def test_transform_transformable_table_header_group(self):
        self.assertRender('test_CssTransforms1', 'transform_transformable_table_header_group')

    def test_transform_transformable_table_row_group(self):
        self.assertRender('test_CssTransforms1', 'transform_transformable_table_row_group')

    def test_transform_transformable_table_row(self):
        self.assertRender('test_CssTransforms1', 'transform_transformable_table_row')

    def test_transform_transformable_table(self):
        self.assertRender('test_CssTransforms1', 'transform_transformable_table')

    def test_transform_translate_001(self):
        self.assertRender('test_CssTransforms1', 'transform_translate_001')

    def test_transform_translate_002(self):
        self.assertRender('test_CssTransforms1', 'transform_translate_002')

    def test_transform_translate_003(self):
        self.assertRender('test_CssTransforms1', 'transform_translate_003')

    def test_transform_translate_004(self):
        self.assertRender('test_CssTransforms1', 'transform_translate_004')

    def test_transform_translate_005(self):
        self.assertRender('test_CssTransforms1', 'transform_translate_005')

    def test_transform_translatex_001(self):
        self.assertRender('test_CssTransforms1', 'transform_translatex_001')

    def test_transform_translatex_002(self):
        self.assertRender('test_CssTransforms1', 'transform_translatex_002')

    def test_transform_translatex_003(self):
        self.assertRender('test_CssTransforms1', 'transform_translatex_003')

    def test_transform_translatex_004(self):
        self.assertRender('test_CssTransforms1', 'transform_translatex_004')

    def test_transform_translatex_005(self):
        self.assertRender('test_CssTransforms1', 'transform_translatex_005')

    def test_transform_translatex_006(self):
        self.assertRender('test_CssTransforms1', 'transform_translatex_006')

    def test_transform_translatey_001(self):
        self.assertRender('test_CssTransforms1', 'transform_translatey_001')

    def test_transform_translatey_002(self):
        self.assertRender('test_CssTransforms1', 'transform_translatey_002')

    def test_transform_translatey_003(self):
        self.assertRender('test_CssTransforms1', 'transform_translatey_003')

    def test_transform_translatey_004(self):
        self.assertRender('test_CssTransforms1', 'transform_translatey_004')

    def test_transform_translatey_005(self):
        self.assertRender('test_CssTransforms1', 'transform_translatey_005')

    def test_transform3d_backface_visibility_001(self):
        self.assertRender('test_CssTransforms1', 'transform3d_backface_visibility_001')

    def test_transform3d_backface_visibility_002(self):
        self.assertRender('test_CssTransforms1', 'transform3d_backface_visibility_002')

    def test_transform3d_backface_visibility_003(self):
        self.assertRender('test_CssTransforms1', 'transform3d_backface_visibility_003')

    def test_transform3d_backface_visibility_004(self):
        self.assertRender('test_CssTransforms1', 'transform3d_backface_visibility_004')

    def test_transform3d_backface_visibility_005(self):
        self.assertRender('test_CssTransforms1', 'transform3d_backface_visibility_005')

    def test_transform3d_backface_visibility_006(self):
        self.assertRender('test_CssTransforms1', 'transform3d_backface_visibility_006')

    def test_transform3d_backface_visibility_007(self):
        self.assertRender('test_CssTransforms1', 'transform3d_backface_visibility_007')

    def test_transform3d_backface_visibility_008(self):
        self.assertRender('test_CssTransforms1', 'transform3d_backface_visibility_008')

    def test_transform3d_image_scale_001(self):
        self.assertRender('test_CssTransforms1', 'transform3d_image_scale_001')

    def test_transform3d_image_scale_002(self):
        self.assertRender('test_CssTransforms1', 'transform3d_image_scale_002')

    def test_transform3d_matrix3d_001(self):
        self.assertRender('test_CssTransforms1', 'transform3d_matrix3d_001')

    def test_transform3d_matrix3d_002(self):
        self.assertRender('test_CssTransforms1', 'transform3d_matrix3d_002')

    def test_transform3d_matrix3d_003(self):
        self.assertRender('test_CssTransforms1', 'transform3d_matrix3d_003')

    def test_transform3d_matrix3d_004(self):
        self.assertRender('test_CssTransforms1', 'transform3d_matrix3d_004')

    def test_transform3d_matrix3d_005(self):
        self.assertRender('test_CssTransforms1', 'transform3d_matrix3d_005')

    def test_transform3d_perspective_001(self):
        self.assertRender('test_CssTransforms1', 'transform3d_perspective_001')

    def test_transform3d_perspective_002(self):
        self.assertRender('test_CssTransforms1', 'transform3d_perspective_002')

    def test_transform3d_perspective_003(self):
        self.assertRender('test_CssTransforms1', 'transform3d_perspective_003')

    def test_transform3d_perspective_004(self):
        self.assertRender('test_CssTransforms1', 'transform3d_perspective_004')

    def test_transform3d_perspective_005(self):
        self.assertRender('test_CssTransforms1', 'transform3d_perspective_005')

    def test_transform3d_perspective_006(self):
        self.assertRender('test_CssTransforms1', 'transform3d_perspective_006')

    def test_transform3d_perspective_007(self):
        self.assertRender('test_CssTransforms1', 'transform3d_perspective_007')

    def test_transform3d_perspective_008(self):
        self.assertRender('test_CssTransforms1', 'transform3d_perspective_008')

    def test_transform3d_perspective_009(self):
        self.assertRender('test_CssTransforms1', 'transform3d_perspective_009')

    def test_transform3d_perspective_origin_001(self):
        self.assertRender('test_CssTransforms1', 'transform3d_perspective_origin_001')

    def test_transform3d_preserve3d_001(self):
        self.assertRender('test_CssTransforms1', 'transform3d_preserve3d_001')

    def test_transform3d_preserve3d_002(self):
        self.assertRender('test_CssTransforms1', 'transform3d_preserve3d_002')

    def test_transform3d_preserve3d_003(self):
        self.assertRender('test_CssTransforms1', 'transform3d_preserve3d_003')

    def test_transform3d_preserve3d_004(self):
        self.assertRender('test_CssTransforms1', 'transform3d_preserve3d_004')

    def test_transform3d_preserve3d_005(self):
        self.assertRender('test_CssTransforms1', 'transform3d_preserve3d_005')

    def test_transform3d_preserve3d_006(self):
        self.assertRender('test_CssTransforms1', 'transform3d_preserve3d_006')

    def test_transform3d_preserve3d_007(self):
        self.assertRender('test_CssTransforms1', 'transform3d_preserve3d_007')

    def test_transform3d_preserve3d_008(self):
        self.assertRender('test_CssTransforms1', 'transform3d_preserve3d_008')

    def test_transform3d_preserve3d_009(self):
        self.assertRender('test_CssTransforms1', 'transform3d_preserve3d_009')

    def test_transform3d_preserve3d_010(self):
        self.assertRender('test_CssTransforms1', 'transform3d_preserve3d_010')

    def test_transform3d_preserve3d_011(self):
        self.assertRender('test_CssTransforms1', 'transform3d_preserve3d_011')

    def test_transform3d_preserve3d_012(self):
        self.assertRender('test_CssTransforms1', 'transform3d_preserve3d_012')

    def test_transform3d_preserve3d_013(self):
        self.assertRender('test_CssTransforms1', 'transform3d_preserve3d_013')

    def test_transform3d_rotate3d_001(self):
        self.assertRender('test_CssTransforms1', 'transform3d_rotate3d_001')

    def test_transform3d_rotate3d_002(self):
        self.assertRender('test_CssTransforms1', 'transform3d_rotate3d_002')

    def test_transform3d_rotatex_001(self):
        self.assertRender('test_CssTransforms1', 'transform3d_rotatex_001')

    def test_transform3d_rotatex_perspective_001(self):
        self.assertRender('test_CssTransforms1', 'transform3d_rotatex_perspective_001')

    def test_transform3d_rotatex_perspective_002(self):
        self.assertRender('test_CssTransforms1', 'transform3d_rotatex_perspective_002')

    def test_transform3d_rotatex_perspective_003(self):
        self.assertRender('test_CssTransforms1', 'transform3d_rotatex_perspective_003')

    def test_transform3d_rotatex_transformorigin_001(self):
        self.assertRender('test_CssTransforms1', 'transform3d_rotatex_transformorigin_001')

    def test_transform3d_rotatey_001(self):
        self.assertRender('test_CssTransforms1', 'transform3d_rotatey_001')

    def test_transform3d_scale_001(self):
        self.assertRender('test_CssTransforms1', 'transform3d_scale_001')

    def test_transform3d_scale_002(self):
        self.assertRender('test_CssTransforms1', 'transform3d_scale_002')

    def test_transform3d_scale_003(self):
        self.assertRender('test_CssTransforms1', 'transform3d_scale_003')

    def test_transform3d_scale_004(self):
        self.assertRender('test_CssTransforms1', 'transform3d_scale_004')

    def test_transform3d_scale_005(self):
        self.assertRender('test_CssTransforms1', 'transform3d_scale_005')

    def test_transform3d_scale_006(self):
        self.assertRender('test_CssTransforms1', 'transform3d_scale_006')

    def test_transform3d_scale_007(self):
        self.assertRender('test_CssTransforms1', 'transform3d_scale_007')

    def test_transform3d_sorting_001(self):
        self.assertRender('test_CssTransforms1', 'transform3d_sorting_001')

    def test_transform3d_sorting_002(self):
        self.assertRender('test_CssTransforms1', 'transform3d_sorting_002')

    def test_transform3d_sorting_003(self):
        self.assertRender('test_CssTransforms1', 'transform3d_sorting_003')

    def test_transform3d_sorting_004(self):
        self.assertRender('test_CssTransforms1', 'transform3d_sorting_004')

    def test_transform3d_sorting_005(self):
        self.assertRender('test_CssTransforms1', 'transform3d_sorting_005')

    def test_transform3d_sorting_006(self):
        self.assertRender('test_CssTransforms1', 'transform3d_sorting_006')

    def test_transform3d_translate3d_001(self):
        self.assertRender('test_CssTransforms1', 'transform3d_translate3d_001')

    def test_transform3d_translatez_001(self):
        self.assertRender('test_CssTransforms1', 'transform3d_translatez_001')

    def test_transform_translate(self):
        self.assertRender('test_CssTransforms1', 'transform_translate')

    def test_transform_translate_invalid(self):
        self.assertRender('test_CssTransforms1', 'transform_translate_invalid')

    def test_transform_translate_max(self):
        self.assertRender('test_CssTransforms1', 'transform_translate_max')

    def test_transform_translate_min(self):
        self.assertRender('test_CssTransforms1', 'transform_translate_min')

    def test_transform_translate_neg(self):
        self.assertRender('test_CssTransforms1', 'transform_translate_neg')

    def test_transform_translate_second_omited(self):
        self.assertRender('test_CssTransforms1', 'transform_translate_second_omited')

    def test_transform_translate_zero(self):
        self.assertRender('test_CssTransforms1', 'transform_translate_zero')

    def test_transforms_rotate_degree_90(self):
        self.assertRender('test_CssTransforms1', 'transforms_rotate_degree_90')

    def test_transforms_rotate_translate_scale(self):
        self.assertRender('test_CssTransforms1', 'transforms_rotate_translate_scale')

    def test_transforms_rotatey_degree_60(self):
        self.assertRender('test_CssTransforms1', 'transforms_rotatey_degree_60')

    def test_transforms_skewx(self):
        self.assertRender('test_CssTransforms1', 'transforms_skewx')

    def test_transforms_skewy(self):
        self.assertRender('test_CssTransforms1', 'transforms_skewy')

    def test_translate_optional_second_001(self):
        self.assertRender('test_CssTransforms1', 'translate_optional_second_001')

    def test_translate(self):
        self.assertRender('test_CssTransforms1', 'translate')

    def test_transofrmed_preserve_3d_1(self):
        self.assertRender('test_CssTransforms1', 'transofrmed_preserve_3d_1')

    def test_transofrmed_rotatex_3(self):
        self.assertRender('test_CssTransforms1', 'transofrmed_rotatex_3')

    def test_transofrmed_rotatey_1(self):
        self.assertRender('test_CssTransforms1', 'transofrmed_rotatey_1')

    def test_ttwf_css_3d_polygon_cycle_mismatch(self):
        self.assertRender('test_CssTransforms1', 'ttwf_css_3d_polygon_cycle_mismatch')

    def test_ttwf_css_3d_polygon_cycle(self):
        self.assertRender('test_CssTransforms1', 'ttwf_css_3d_polygon_cycle')

    def test_ttwf_reftest_rotate(self):
        self.assertRender('test_CssTransforms1', 'ttwf_reftest_rotate')

    def test_ttwf_transform_skewx_001(self):
        self.assertRender('test_CssTransforms1', 'ttwf_transform_skewx_001')

    def test_ttwf_transform_skewy_001(self):
        self.assertRender('test_CssTransforms1', 'ttwf_transform_skewy_001')

    def test_ttwf_transform_translatex_001(self):
        self.assertRender('test_CssTransforms1', 'ttwf_transform_translatex_001')

    def test_ttwf_transform_translatey_001(self):
        self.assertRender('test_CssTransforms1', 'ttwf_transform_translatey_001')

    def test_video_001(self):
        self.assertRender('test_CssTransforms1', 'video_001')

