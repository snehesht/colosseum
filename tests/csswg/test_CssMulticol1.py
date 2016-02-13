from unittest import expectedFailure
from .. utils import CSSWGTestCase

class test_CssMulticol1(CSSWGTestCase):
    def test_break_before_always_001(self):
        self.assertRender('test_CssMulticol1', 'break_before_always_001')

    def test_grid_inline_multicol_001(self):
        self.assertRender('test_CssMulticol1', 'grid_inline_multicol_001')

    def test_grid_multicol_001(self):
        self.assertRender('test_CssMulticol1', 'grid_multicol_001')

    def test_multicol_basic_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_basic_001')

    def test_multicol_basic_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_basic_002')

    def test_multicol_basic_003(self):
        self.assertRender('test_CssMulticol1', 'multicol_basic_003')

    def test_multicol_basic_004(self):
        self.assertRender('test_CssMulticol1', 'multicol_basic_004')

    def test_multicol_block_clip_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_block_clip_001')

    def test_multicol_block_clip_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_block_clip_002')

    def test_multicol_br_inside_avoidcolumn_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_br_inside_avoidcolumn_001')

    def test_multicol_break_000(self):
        self.assertRender('test_CssMulticol1', 'multicol_break_000')

    def test_multicol_break_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_break_001')

    def test_multicol_clip_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_clip_001')

    def test_multicol_clip_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_clip_002')

    def test_multicol_collapsing_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_collapsing_001')

    def test_multicol_columns_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_columns_001')

    def test_multicol_columns_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_columns_002')

    def test_multicol_columns_003(self):
        self.assertRender('test_CssMulticol1', 'multicol_columns_003')

    def test_multicol_columns_004(self):
        self.assertRender('test_CssMulticol1', 'multicol_columns_004')

    def test_multicol_columns_005(self):
        self.assertRender('test_CssMulticol1', 'multicol_columns_005')

    def test_multicol_columns_006(self):
        self.assertRender('test_CssMulticol1', 'multicol_columns_006')

    def test_multicol_columns_007(self):
        self.assertRender('test_CssMulticol1', 'multicol_columns_007')

    def test_multicol_columns_invalid_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_columns_invalid_001')

    def test_multicol_columns_invalid_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_columns_invalid_002')

    def test_multicol_columns_toolong_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_columns_toolong_001')

    def test_multicol_containing_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_containing_001')

    def test_multicol_containing_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_containing_002')

    def test_multicol_count_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_count_001')

    def test_multicol_count_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_count_002')

    def test_multicol_count_computed_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_count_computed_001')

    def test_multicol_count_computed_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_count_computed_002')

    def test_multicol_count_computed_003(self):
        self.assertRender('test_CssMulticol1', 'multicol_count_computed_003')

    def test_multicol_count_computed_004(self):
        self.assertRender('test_CssMulticol1', 'multicol_count_computed_004')

    def test_multicol_count_computed_005(self):
        self.assertRender('test_CssMulticol1', 'multicol_count_computed_005')

    def test_multicol_count_large_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_count_large_001')

    def test_multicol_count_large_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_count_large_002')

    def test_multicol_count_negative_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_count_negative_001')

    def test_multicol_count_negative_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_count_negative_002')

    def test_multicol_count_non_integer_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_count_non_integer_001')

    def test_multicol_count_non_integer_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_count_non_integer_002')

    def test_multicol_count_non_integer_003(self):
        self.assertRender('test_CssMulticol1', 'multicol_count_non_integer_003')

    def test_multicol_fill_000(self):
        self.assertRender('test_CssMulticol1', 'multicol_fill_000')

    def test_multicol_fill_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_fill_001')

    def test_multicol_fill_auto_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_fill_auto_001')

    def test_multicol_fill_auto_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_fill_auto_002')

    def test_multicol_fill_auto_003(self):
        self.assertRender('test_CssMulticol1', 'multicol_fill_auto_003')

    def test_multicol_fill_auto_block_children_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_fill_auto_block_children_001')

    def test_multicol_fill_auto_block_children_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_fill_auto_block_children_002')

    def test_multicol_fill_auto(self):
        self.assertRender('test_CssMulticol1', 'multicol_fill_auto')

    def test_multicol_fill_balance_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_fill_balance_001')

    def test_multicol_gap_000(self):
        self.assertRender('test_CssMulticol1', 'multicol_gap_000')

    def test_multicol_gap_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_gap_001')

    def test_multicol_gap_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_gap_002')

    def test_multicol_gap_003(self):
        self.assertRender('test_CssMulticol1', 'multicol_gap_003')

    def test_multicol_gap_fraction_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_gap_fraction_001')

    def test_multicol_gap_large_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_gap_large_001')

    def test_multicol_gap_large_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_gap_large_002')

    def test_multicol_gap_negative_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_gap_negative_001')

    def test_multicol_height_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_height_001')

    def test_multicol_height_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_height_002')

    def test_multicol_height_block_child_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_height_block_child_001')

    def test_multicol_inherit_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_inherit_001')

    def test_multicol_inherit_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_inherit_002')

    def test_multicol_inherit_003(self):
        self.assertRender('test_CssMulticol1', 'multicol_inherit_003')

    def test_multicol_inherit_004(self):
        self.assertRender('test_CssMulticol1', 'multicol_inherit_004')

    def test_multicol_list_item_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_list_item_001')

    def test_multicol_margin_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_margin_001')

    def test_multicol_margin_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_margin_002')

    def test_multicol_margin_child_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_margin_child_001')

    def test_multicol_nested_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_nested_002')

    def test_multicol_nested_005(self):
        self.assertRender('test_CssMulticol1', 'multicol_nested_005')

    def test_multicol_nested_column_rule_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_nested_column_rule_001')

    def test_multicol_nested_margin_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_nested_margin_001')

    def test_multicol_nested_margin_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_nested_margin_002')

    def test_multicol_nested_margin_003(self):
        self.assertRender('test_CssMulticol1', 'multicol_nested_margin_003')

    def test_multicol_nested_margin_004(self):
        self.assertRender('test_CssMulticol1', 'multicol_nested_margin_004')

    def test_multicol_nested_margin_005(self):
        self.assertRender('test_CssMulticol1', 'multicol_nested_margin_005')

    def test_multicol_overflow_000(self):
        self.assertRender('test_CssMulticol1', 'multicol_overflow_000')

    def test_multicol_overflowing_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_overflowing_001')

    def test_multicol_reduce_000(self):
        self.assertRender('test_CssMulticol1', 'multicol_reduce_000')

    def test_multicol_rule_000(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_000')

    def test_multicol_rule_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_001')

    def test_multicol_rule_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_002')

    def test_multicol_rule_003(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_003')

    def test_multicol_rule_004(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_004')

    def test_multicol_rule_color_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_color_001')

    def test_multicol_rule_color_inherit_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_color_inherit_001')

    def test_multicol_rule_color_inherit_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_color_inherit_002')

    def test_multicol_rule_dashed_000(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_dashed_000')

    def test_multicol_rule_dotted_000(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_dotted_000')

    def test_multicol_rule_double_000(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_double_000')

    def test_multicol_rule_fraction_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_fraction_001')

    def test_multicol_rule_fraction_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_fraction_002')

    def test_multicol_rule_fraction_003(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_fraction_003')

    def test_multicol_rule_groove_000(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_groove_000')

    def test_multicol_rule_hidden_000(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_hidden_000')

    def test_multicol_rule_inset_000(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_inset_000')

    def test_multicol_rule_large_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_large_001')

    def test_multicol_rule_large_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_large_002')

    def test_multicol_rule_none_000(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_none_000')

    def test_multicol_rule_outset_000(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_outset_000')

    def test_multicol_rule_percent_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_percent_001')

    def test_multicol_rule_px_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_px_001')

    def test_multicol_rule_ridge_000(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_ridge_000')

    def test_multicol_rule_samelength_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_samelength_001')

    def test_multicol_rule_shorthand_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_shorthand_001')

    def test_multicol_rule_solid_000(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_solid_000')

    def test_multicol_rule_stacking_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_stacking_001')

    def test_multicol_rule_style_groove_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_style_groove_001')

    def test_multicol_rule_style_inset_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_style_inset_001')

    def test_multicol_rule_style_outset_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_style_outset_001')

    def test_multicol_rule_style_ridge_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_rule_style_ridge_001')

    def test_multicol_shorthand_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_shorthand_001')

    def test_multicol_span_000(self):
        self.assertRender('test_CssMulticol1', 'multicol_span_000')

    def test_multicol_span_all_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_span_all_001')

    def test_multicol_span_all_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_span_all_002')

    def test_multicol_span_all_003(self):
        self.assertRender('test_CssMulticol1', 'multicol_span_all_003')

    def test_multicol_span_all_block_sibling_003(self):
        self.assertRender('test_CssMulticol1', 'multicol_span_all_block_sibling_003')

    def test_multicol_span_all_child_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_span_all_child_001')

    def test_multicol_span_all_child_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_span_all_child_002')

    def test_multicol_span_all_margin_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_span_all_margin_001')

    def test_multicol_span_all_margin_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_span_all_margin_002')

    def test_multicol_span_all_margin_bottom_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_span_all_margin_bottom_001')

    def test_multicol_span_all_margin_nested_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_span_all_margin_nested_001')

    def test_multicol_span_all_margin_nested_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_span_all_margin_nested_002')

    def test_multicol_span_all_margin_nested_003(self):
        self.assertRender('test_CssMulticol1', 'multicol_span_all_margin_nested_003')

    def test_multicol_span_all_margin_nested_firstchild_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_span_all_margin_nested_firstchild_001')

    def test_multicol_span_float_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_span_float_001')

    def test_multicol_span_none_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_span_none_001')

    def test_multicol_table_cell_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_table_cell_001')

    def test_multicol_table_cell_height_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_table_cell_height_001')

    def test_multicol_table_cell_height_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_table_cell_height_002')

    def test_multicol_table_cell_vertical_align_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_table_cell_vertical_align_001')

    def test_multicol_width_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_width_001')

    def test_multicol_width_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_width_002')

    def test_multicol_width_003(self):
        self.assertRender('test_CssMulticol1', 'multicol_width_003')

    def test_multicol_width_count_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_width_count_001')

    def test_multicol_width_count_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_width_count_002')

    def test_multicol_width_ems_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_width_ems_001')

    def test_multicol_width_invalid_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_width_invalid_001')

    def test_multicol_width_large_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_width_large_001')

    def test_multicol_width_large_002(self):
        self.assertRender('test_CssMulticol1', 'multicol_width_large_002')

    def test_multicol_width_negative_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_width_negative_001')

    def test_multicol_width_small_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_width_small_001')

    def test_multicol_zero_height_001(self):
        self.assertRender('test_CssMulticol1', 'multicol_zero_height_001')

    def test_regions_multicol_003(self):
        self.assertRender('test_CssMulticol1', 'regions_multicol_003')

    def test_regions_multicol_004(self):
        self.assertRender('test_CssMulticol1', 'regions_multicol_004')

    def test_regions_multicol_006(self):
        self.assertRender('test_CssMulticol1', 'regions_multicol_006')

    def test_regions_multicol_008(self):
        self.assertRender('test_CssMulticol1', 'regions_multicol_008')

    def test_regions_multicol_009(self):
        self.assertRender('test_CssMulticol1', 'regions_multicol_009')

    def test_regions_multicol_011(self):
        self.assertRender('test_CssMulticol1', 'regions_multicol_011')

    def test_regions_multicol_012(self):
        self.assertRender('test_CssMulticol1', 'regions_multicol_012')

    def test_regions_multicol_013(self):
        self.assertRender('test_CssMulticol1', 'regions_multicol_013')

    def test_regions_multicol_015(self):
        self.assertRender('test_CssMulticol1', 'regions_multicol_015')

    def test_regions_multicol_016(self):
        self.assertRender('test_CssMulticol1', 'regions_multicol_016')

    def test_regions_multicol_017(self):
        self.assertRender('test_CssMulticol1', 'regions_multicol_017')

    def test_regions_multicol_019(self):
        self.assertRender('test_CssMulticol1', 'regions_multicol_019')

    def test_regions_multicol_021(self):
        self.assertRender('test_CssMulticol1', 'regions_multicol_021')

    def test_regions_multicol_022(self):
        self.assertRender('test_CssMulticol1', 'regions_multicol_022')

    def test_regions_multicol_023(self):
        self.assertRender('test_CssMulticol1', 'regions_multicol_023')

    def test_regions_multicol_024(self):
        self.assertRender('test_CssMulticol1', 'regions_multicol_024')

    def test_regions_multicol_025(self):
        self.assertRender('test_CssMulticol1', 'regions_multicol_025')

    def test_regions_multicol_026(self):
        self.assertRender('test_CssMulticol1', 'regions_multicol_026')

    def test_regions_multicol_027(self):
        self.assertRender('test_CssMulticol1', 'regions_multicol_027')

    def test_regions_multicol_028(self):
        self.assertRender('test_CssMulticol1', 'regions_multicol_028')

    def test_regions_multicol_029(self):
        self.assertRender('test_CssMulticol1', 'regions_multicol_029')

