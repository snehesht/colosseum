from unittest import expectedFailure
from .. utils import CSSWGTestCase

class test_CssValues3(CSSWGTestCase):
    def test_absolute_length_units(self):
        self.assertRender('test_CssValues3', 'absolute_length_units')

    def test_attr_color_invalid_cast(self):
        self.assertRender('test_CssValues3', 'attr_color_invalid_cast')

    def test_attr_color_invalid_fallback(self):
        self.assertRender('test_CssValues3', 'attr_color_invalid_fallback')

    def test_attr_color_valid(self):
        self.assertRender('test_CssValues3', 'attr_color_valid')

    def test_attr_invalid_type_001(self):
        self.assertRender('test_CssValues3', 'attr_invalid_type_001')

    def test_attr_invalid_type_002(self):
        self.assertRender('test_CssValues3', 'attr_invalid_type_002')

    def test_attr_invalid_type_003(self):
        self.assertRender('test_CssValues3', 'attr_invalid_type_003')

    def test_attr_length_invalid_cast(self):
        self.assertRender('test_CssValues3', 'attr_length_invalid_cast')

    def test_attr_length_invalid_fallback(self):
        self.assertRender('test_CssValues3', 'attr_length_invalid_fallback')

    def test_attr_length_valid_zero_nofallback(self):
        self.assertRender('test_CssValues3', 'attr_length_valid_zero_nofallback')

    def test_attr_length_valid_zero(self):
        self.assertRender('test_CssValues3', 'attr_length_valid_zero')

    def test_attr_length_valid(self):
        self.assertRender('test_CssValues3', 'attr_length_valid')

    def test_attr_px_invalid_cast(self):
        self.assertRender('test_CssValues3', 'attr_px_invalid_cast')

    def test_attr_px_invalid_fallback(self):
        self.assertRender('test_CssValues3', 'attr_px_invalid_fallback')

    def test_attr_px_valid(self):
        self.assertRender('test_CssValues3', 'attr_px_valid')

    def test_calc_background_image_gradient_1(self):
        self.assertRender('test_CssValues3', 'calc_background_image_gradient_1')

    def test_calc_background_linear_gradient_1(self):
        self.assertRender('test_CssValues3', 'calc_background_linear_gradient_1')

    def test_calc_background_position_1(self):
        self.assertRender('test_CssValues3', 'calc_background_position_1')

    def test_calc_background_size_1(self):
        self.assertRender('test_CssValues3', 'calc_background_size_1')

    def test_calc_border_radius_1(self):
        self.assertRender('test_CssValues3', 'calc_border_radius_1')

    def test_calc_height_block_1(self):
        self.assertRender('test_CssValues3', 'calc_height_block_1')

    def test_calc_height_table_1(self):
        self.assertRender('test_CssValues3', 'calc_height_table_1')

    def test_calc_in_calc(self):
        self.assertRender('test_CssValues3', 'calc_in_calc')

    def test_calc_in_media_queries_001(self):
        self.assertRender('test_CssValues3', 'calc_in_media_queries_001')

    def test_calc_in_media_queries_002(self):
        self.assertRender('test_CssValues3', 'calc_in_media_queries_002')

    def test_calc_invalid_range_clamping(self):
        self.assertRender('test_CssValues3', 'calc_invalid_range_clamping')

    def test_calc_margin_block_1(self):
        self.assertRender('test_CssValues3', 'calc_margin_block_1')

    def test_calc_max_height_block_1(self):
        self.assertRender('test_CssValues3', 'calc_max_height_block_1')

    def test_calc_max_width_block_1(self):
        self.assertRender('test_CssValues3', 'calc_max_width_block_1')

    def test_calc_max_width_block_intrinsic_1(self):
        self.assertRender('test_CssValues3', 'calc_max_width_block_intrinsic_1')

    def test_calc_min_height_block_1(self):
        self.assertRender('test_CssValues3', 'calc_min_height_block_1')

    def test_calc_min_width_block_1(self):
        self.assertRender('test_CssValues3', 'calc_min_width_block_1')

    def test_calc_min_width_block_intrinsic_1(self):
        self.assertRender('test_CssValues3', 'calc_min_width_block_intrinsic_1')

    def test_calc_offsets_absolute_bottom_1(self):
        self.assertRender('test_CssValues3', 'calc_offsets_absolute_bottom_1')

    def test_calc_offsets_absolute_left_1(self):
        self.assertRender('test_CssValues3', 'calc_offsets_absolute_left_1')

    def test_calc_offsets_absolute_right_1(self):
        self.assertRender('test_CssValues3', 'calc_offsets_absolute_right_1')

    def test_calc_offsets_absolute_top_1(self):
        self.assertRender('test_CssValues3', 'calc_offsets_absolute_top_1')

    def test_calc_offsets_relative_bottom_1(self):
        self.assertRender('test_CssValues3', 'calc_offsets_relative_bottom_1')

    def test_calc_offsets_relative_left_1(self):
        self.assertRender('test_CssValues3', 'calc_offsets_relative_left_1')

    def test_calc_offsets_relative_right_1(self):
        self.assertRender('test_CssValues3', 'calc_offsets_relative_right_1')

    def test_calc_offsets_relative_top_1(self):
        self.assertRender('test_CssValues3', 'calc_offsets_relative_top_1')

    def test_calc_padding_block_1(self):
        self.assertRender('test_CssValues3', 'calc_padding_block_1')

    def test_calc_parenthesis_stack(self):
        self.assertRender('test_CssValues3', 'calc_parenthesis_stack')

    def test_calc_text_indent_1(self):
        self.assertRender('test_CssValues3', 'calc_text_indent_1')

    def test_calc_text_indent_intrinsic_1(self):
        self.assertRender('test_CssValues3', 'calc_text_indent_intrinsic_1')

    def test_calc_transform_origin_1(self):
        self.assertRender('test_CssValues3', 'calc_transform_origin_1')

    def test_calc_unit_analysis(self):
        self.assertRender('test_CssValues3', 'calc_unit_analysis')

    def test_calc_vertical_align_1(self):
        self.assertRender('test_CssValues3', 'calc_vertical_align_1')

    def test_calc_width_block_1(self):
        self.assertRender('test_CssValues3', 'calc_width_block_1')

    def test_calc_width_block_intrinsic_1(self):
        self.assertRender('test_CssValues3', 'calc_width_block_intrinsic_1')

    def test_calc_width_table_auto_1(self):
        self.assertRender('test_CssValues3', 'calc_width_table_auto_1')

    def test_calc_width_table_fixed_1(self):
        self.assertRender('test_CssValues3', 'calc_width_table_fixed_1')

    def test_ch_unit_001(self):
        self.assertRender('test_CssValues3', 'ch_unit_001')

    def test_initial_background_color(self):
        self.assertRender('test_CssValues3', 'initial_background_color')

    def test_min_width_001(self):
        self.assertRender('test_CssValues3', 'min_width_001')

    def test_mq_calc_001(self):
        self.assertRender('test_CssValues3', 'mq_calc_001')

    def test_mq_calc_002(self):
        self.assertRender('test_CssValues3', 'mq_calc_002')

    def test_mq_calc_003(self):
        self.assertRender('test_CssValues3', 'mq_calc_003')

    def test_mq_calc_004(self):
        self.assertRender('test_CssValues3', 'mq_calc_004')

    def test_mq_calc_005(self):
        self.assertRender('test_CssValues3', 'mq_calc_005')

    def test_multicol_count_non_integer_001(self):
        self.assertRender('test_CssValues3', 'multicol_count_non_integer_001')

    def test_multicol_count_non_integer_002(self):
        self.assertRender('test_CssValues3', 'multicol_count_non_integer_002')

    def test_multicol_count_non_integer_003(self):
        self.assertRender('test_CssValues3', 'multicol_count_non_integer_003')

    def test_multicol_inherit_002(self):
        self.assertRender('test_CssValues3', 'multicol_inherit_002')

    def test_multicol_rule_color_inherit_001(self):
        self.assertRender('test_CssValues3', 'multicol_rule_color_inherit_001')

    def test_multicol_rule_color_inherit_002(self):
        self.assertRender('test_CssValues3', 'multicol_rule_color_inherit_002')

    def test_regions_resizing_003(self):
        self.assertRender('test_CssValues3', 'regions_resizing_003')

    def test_regions_resizing_007(self):
        self.assertRender('test_CssValues3', 'regions_resizing_007')

    def test_regions_resizing_009(self):
        self.assertRender('test_CssValues3', 'regions_resizing_009')

    def test_shape_outside_circle_002(self):
        self.assertRender('test_CssValues3', 'shape_outside_circle_002')

    def test_shape_outside_circle_004(self):
        self.assertRender('test_CssValues3', 'shape_outside_circle_004')

    def test_shape_outside_circle_010(self):
        self.assertRender('test_CssValues3', 'shape_outside_circle_010')

    def test_shape_outside_circle_011(self):
        self.assertRender('test_CssValues3', 'shape_outside_circle_011')

    def test_shape_outside_ellipse_002(self):
        self.assertRender('test_CssValues3', 'shape_outside_ellipse_002')

    def test_shape_outside_ellipse_004(self):
        self.assertRender('test_CssValues3', 'shape_outside_ellipse_004')

    def test_shape_outside_ellipse_010(self):
        self.assertRender('test_CssValues3', 'shape_outside_ellipse_010')

    def test_shape_outside_ellipse_011(self):
        self.assertRender('test_CssValues3', 'shape_outside_ellipse_011')

    def test_shape_outside_inset_003(self):
        self.assertRender('test_CssValues3', 'shape_outside_inset_003')

    def test_shape_outside_inset_008(self):
        self.assertRender('test_CssValues3', 'shape_outside_inset_008')

    def test_shape_outside_inset_009(self):
        self.assertRender('test_CssValues3', 'shape_outside_inset_009')

    def test_shape_outside_polygon_004(self):
        self.assertRender('test_CssValues3', 'shape_outside_polygon_004')

    def test_shape_outside_polygon_006(self):
        self.assertRender('test_CssValues3', 'shape_outside_polygon_006')

    def test_transition_delay_001(self):
        self.assertRender('test_CssValues3', 'transition_delay_001')

    def test_transition_duration_001(self):
        self.assertRender('test_CssValues3', 'transition_duration_001')

    def test_vh_calc_support_pct(self):
        self.assertRender('test_CssValues3', 'vh_calc_support_pct')

    def test_vh_calc_support(self):
        self.assertRender('test_CssValues3', 'vh_calc_support')

    def test_vh_em_inherit(self):
        self.assertRender('test_CssValues3', 'vh_em_inherit')

    def test_vh_inherit(self):
        self.assertRender('test_CssValues3', 'vh_inherit')

    def test_vh_interpolate_pct(self):
        self.assertRender('test_CssValues3', 'vh_interpolate_pct')

    def test_vh_interpolate_px(self):
        self.assertRender('test_CssValues3', 'vh_interpolate_px')

    def test_vh_interpolate_vh(self):
        self.assertRender('test_CssValues3', 'vh_interpolate_vh')

    def test_vh_support_atviewport(self):
        self.assertRender('test_CssValues3', 'vh_support_atviewport')

    def test_vh_support_margin(self):
        self.assertRender('test_CssValues3', 'vh_support_margin')

    def test_vh_support_transform_origin(self):
        self.assertRender('test_CssValues3', 'vh_support_transform_origin')

    def test_vh_support_transform_translate(self):
        self.assertRender('test_CssValues3', 'vh_support_transform_translate')

    def test_vh_support(self):
        self.assertRender('test_CssValues3', 'vh_support')

    def test_vh_zero_support(self):
        self.assertRender('test_CssValues3', 'vh_zero_support')

    def test_vh_not_refreshing_on_chrome(self):
        self.assertRender('test_CssValues3', 'vh_not_refreshing_on_chrome')

    def test_vh_not_refreshing_on_chrome_iframe(self):
        self.assertRender('test_CssValues3', 'vh_not_refreshing_on_chrome_iframe')

    def test_viewport_relative_lengths_scaled_viewport(self):
        self.assertRender('test_CssValues3', 'viewport_relative_lengths_scaled_viewport')

    def test_viewport_units_css2_001(self):
        self.assertRender('test_CssValues3', 'viewport_units_css2_001')

