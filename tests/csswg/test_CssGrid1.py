from unittest import expectedFailure
from .. utils import CSSWGTestCase

class test_CssGrid1(CSSWGTestCase):
    def test_display_grid(self):
        self.assertRender('test_CssGrid1', 'display_grid')

    def test_display_inline_grid(self):
        self.assertRender('test_CssGrid1', 'display_inline_grid')

    def test_fr_unit_with_percentage(self):
        self.assertRender('test_CssGrid1', 'fr_unit_with_percentage')

    def test_fr_unit(self):
        self.assertRender('test_CssGrid1', 'fr_unit')

    def test_grid_computed_value_display_floated_items_001(self):
        self.assertRender('test_CssGrid1', 'grid_computed_value_display_floated_items_001')

    def test_grid_display_grid_001(self):
        self.assertRender('test_CssGrid1', 'grid_display_grid_001')

    def test_grid_display_inline_grid_001(self):
        self.assertRender('test_CssGrid1', 'grid_display_inline_grid_001')

    def test_grid_first_letter_001(self):
        self.assertRender('test_CssGrid1', 'grid_first_letter_001')

    def test_grid_first_letter_002(self):
        self.assertRender('test_CssGrid1', 'grid_first_letter_002')

    def test_grid_first_letter_003(self):
        self.assertRender('test_CssGrid1', 'grid_first_letter_003')

    def test_grid_first_line_001(self):
        self.assertRender('test_CssGrid1', 'grid_first_line_001')

    def test_grid_first_line_002(self):
        self.assertRender('test_CssGrid1', 'grid_first_line_002')

    def test_grid_first_line_003(self):
        self.assertRender('test_CssGrid1', 'grid_first_line_003')

    def test_grid_float_001(self):
        self.assertRender('test_CssGrid1', 'grid_float_001')

    def test_grid_floats_no_intrude_001(self):
        self.assertRender('test_CssGrid1', 'grid_floats_no_intrude_001')

    def test_grid_inline_first_letter_001(self):
        self.assertRender('test_CssGrid1', 'grid_inline_first_letter_001')

    def test_grid_inline_first_letter_002(self):
        self.assertRender('test_CssGrid1', 'grid_inline_first_letter_002')

    def test_grid_inline_first_letter_003(self):
        self.assertRender('test_CssGrid1', 'grid_inline_first_letter_003')

    def test_grid_inline_first_line_001(self):
        self.assertRender('test_CssGrid1', 'grid_inline_first_line_001')

    def test_grid_inline_first_line_002(self):
        self.assertRender('test_CssGrid1', 'grid_inline_first_line_002')

    def test_grid_inline_first_line_003(self):
        self.assertRender('test_CssGrid1', 'grid_inline_first_line_003')

    def test_grid_inline_float_001(self):
        self.assertRender('test_CssGrid1', 'grid_inline_float_001')

    def test_grid_inline_floats_no_intrude_001(self):
        self.assertRender('test_CssGrid1', 'grid_inline_floats_no_intrude_001')

    def test_grid_inline_items_001(self):
        self.assertRender('test_CssGrid1', 'grid_inline_items_001')

    def test_grid_inline_items_002(self):
        self.assertRender('test_CssGrid1', 'grid_inline_items_002')

    def test_grid_inline_items_003(self):
        self.assertRender('test_CssGrid1', 'grid_inline_items_003')

    def test_grid_inline_items_inline_blocks_001(self):
        self.assertRender('test_CssGrid1', 'grid_inline_items_inline_blocks_001')

    def test_grid_inline_margins_no_collapse_001(self):
        self.assertRender('test_CssGrid1', 'grid_inline_margins_no_collapse_001')

    def test_grid_inline_multicol_001(self):
        self.assertRender('test_CssGrid1', 'grid_inline_multicol_001')

    def test_grid_inline_order_property_auto_placement_001(self):
        self.assertRender('test_CssGrid1', 'grid_inline_order_property_auto_placement_001')

    def test_grid_inline_order_property_auto_placement_002(self):
        self.assertRender('test_CssGrid1', 'grid_inline_order_property_auto_placement_002')

    def test_grid_inline_order_property_auto_placement_003(self):
        self.assertRender('test_CssGrid1', 'grid_inline_order_property_auto_placement_003')

    def test_grid_inline_order_property_auto_placement_004(self):
        self.assertRender('test_CssGrid1', 'grid_inline_order_property_auto_placement_004')

    def test_grid_inline_order_property_auto_placement_005(self):
        self.assertRender('test_CssGrid1', 'grid_inline_order_property_auto_placement_005')

    def test_grid_inline_order_property_painting_001(self):
        self.assertRender('test_CssGrid1', 'grid_inline_order_property_painting_001')

    def test_grid_inline_order_property_painting_002(self):
        self.assertRender('test_CssGrid1', 'grid_inline_order_property_painting_002')

    def test_grid_inline_order_property_painting_003(self):
        self.assertRender('test_CssGrid1', 'grid_inline_order_property_painting_003')

    def test_grid_inline_order_property_painting_004(self):
        self.assertRender('test_CssGrid1', 'grid_inline_order_property_painting_004')

    def test_grid_inline_order_property_painting_005(self):
        self.assertRender('test_CssGrid1', 'grid_inline_order_property_painting_005')

    def test_grid_inline_support_flexible_lengths_001(self):
        self.assertRender('test_CssGrid1', 'grid_inline_support_flexible_lengths_001')

    def test_grid_inline_support_grid_template_areas_001(self):
        self.assertRender('test_CssGrid1', 'grid_inline_support_grid_template_areas_001')

    def test_grid_inline_support_grid_template_columns_rows_001(self):
        self.assertRender('test_CssGrid1', 'grid_inline_support_grid_template_columns_rows_001')

    def test_grid_inline_support_named_grid_lines_001(self):
        self.assertRender('test_CssGrid1', 'grid_inline_support_named_grid_lines_001')

    def test_grid_inline_support_repeat_001(self):
        self.assertRender('test_CssGrid1', 'grid_inline_support_repeat_001')

    def test_grid_inline_template_columns_rows_resolved_values_001(self):
        self.assertRender('test_CssGrid1', 'grid_inline_template_columns_rows_resolved_values_001')

    def test_grid_inline_vertical_align_001(self):
        self.assertRender('test_CssGrid1', 'grid_inline_vertical_align_001')

    def test_grid_inline_z_axis_ordering_001(self):
        self.assertRender('test_CssGrid1', 'grid_inline_z_axis_ordering_001')

    def test_grid_inline_z_axis_ordering_002(self):
        self.assertRender('test_CssGrid1', 'grid_inline_z_axis_ordering_002')

    def test_grid_inline_z_axis_ordering_003(self):
        self.assertRender('test_CssGrid1', 'grid_inline_z_axis_ordering_003')

    def test_grid_inline_z_axis_ordering_004(self):
        self.assertRender('test_CssGrid1', 'grid_inline_z_axis_ordering_004')

    def test_grid_inline_z_axis_ordering_005(self):
        self.assertRender('test_CssGrid1', 'grid_inline_z_axis_ordering_005')

    def test_grid_inline_z_axis_ordering_overlapped_items_001(self):
        self.assertRender('test_CssGrid1', 'grid_inline_z_axis_ordering_overlapped_items_001')

    def test_grid_inline_z_axis_ordering_overlapped_items_002(self):
        self.assertRender('test_CssGrid1', 'grid_inline_z_axis_ordering_overlapped_items_002')

    def test_grid_inline_z_axis_ordering_overlapped_items_003(self):
        self.assertRender('test_CssGrid1', 'grid_inline_z_axis_ordering_overlapped_items_003')

    def test_grid_inline_z_axis_ordering_overlapped_items_004(self):
        self.assertRender('test_CssGrid1', 'grid_inline_z_axis_ordering_overlapped_items_004')

    def test_grid_inline_z_axis_ordering_overlapped_items_005(self):
        self.assertRender('test_CssGrid1', 'grid_inline_z_axis_ordering_overlapped_items_005')

    def test_grid_inline_z_axis_ordering_overlapped_items_006(self):
        self.assertRender('test_CssGrid1', 'grid_inline_z_axis_ordering_overlapped_items_006')

    def test_grid_items_001(self):
        self.assertRender('test_CssGrid1', 'grid_items_001')

    def test_grid_items_002(self):
        self.assertRender('test_CssGrid1', 'grid_items_002')

    def test_grid_items_003(self):
        self.assertRender('test_CssGrid1', 'grid_items_003')

    def test_grid_items_inline_blocks_001(self):
        self.assertRender('test_CssGrid1', 'grid_items_inline_blocks_001')

    def test_grid_layout_auto_tracks(self):
        self.assertRender('test_CssGrid1', 'grid_layout_auto_tracks')

    def test_grid_layout_basic(self):
        self.assertRender('test_CssGrid1', 'grid_layout_basic')

    def test_grid_layout_free_space_unit(self):
        self.assertRender('test_CssGrid1', 'grid_layout_free_space_unit')

    def test_grid_layout_grid_span(self):
        self.assertRender('test_CssGrid1', 'grid_layout_grid_span')

    def test_grid_layout_lines_shorthands(self):
        self.assertRender('test_CssGrid1', 'grid_layout_lines_shorthands')

    def test_grid_layout_lines(self):
        self.assertRender('test_CssGrid1', 'grid_layout_lines')

    def test_grid_layout_placement_shorthands(self):
        self.assertRender('test_CssGrid1', 'grid_layout_placement_shorthands')

    def test_grid_layout_properties(self):
        self.assertRender('test_CssGrid1', 'grid_layout_properties')

    def test_grid_layout_repeat_notation(self):
        self.assertRender('test_CssGrid1', 'grid_layout_repeat_notation')

    def test_grid_layout_z_order_a(self):
        self.assertRender('test_CssGrid1', 'grid_layout_z_order_a')

    def test_grid_layout_z_order_b(self):
        self.assertRender('test_CssGrid1', 'grid_layout_z_order_b')

    def test_grid_margins_no_collapse_001(self):
        self.assertRender('test_CssGrid1', 'grid_margins_no_collapse_001')

    def test_grid_minimum_size_grid_items_001(self):
        self.assertRender('test_CssGrid1', 'grid_minimum_size_grid_items_001')

    def test_grid_minimum_size_grid_items_002(self):
        self.assertRender('test_CssGrid1', 'grid_minimum_size_grid_items_002')

    def test_grid_minimum_size_grid_items_003(self):
        self.assertRender('test_CssGrid1', 'grid_minimum_size_grid_items_003')

    def test_grid_minimum_size_grid_items_004(self):
        self.assertRender('test_CssGrid1', 'grid_minimum_size_grid_items_004')

    def test_grid_minimum_size_grid_items_005(self):
        self.assertRender('test_CssGrid1', 'grid_minimum_size_grid_items_005')

    def test_grid_minimum_size_grid_items_006(self):
        self.assertRender('test_CssGrid1', 'grid_minimum_size_grid_items_006')

    def test_grid_minimum_size_grid_items_007(self):
        self.assertRender('test_CssGrid1', 'grid_minimum_size_grid_items_007')

    def test_grid_minimum_size_grid_items_008(self):
        self.assertRender('test_CssGrid1', 'grid_minimum_size_grid_items_008')

    def test_grid_minimum_size_grid_items_009(self):
        self.assertRender('test_CssGrid1', 'grid_minimum_size_grid_items_009')

    def test_grid_multicol_001(self):
        self.assertRender('test_CssGrid1', 'grid_multicol_001')

    def test_grid_order_property_auto_placement_001(self):
        self.assertRender('test_CssGrid1', 'grid_order_property_auto_placement_001')

    def test_grid_order_property_auto_placement_002(self):
        self.assertRender('test_CssGrid1', 'grid_order_property_auto_placement_002')

    def test_grid_order_property_auto_placement_003(self):
        self.assertRender('test_CssGrid1', 'grid_order_property_auto_placement_003')

    def test_grid_order_property_auto_placement_004(self):
        self.assertRender('test_CssGrid1', 'grid_order_property_auto_placement_004')

    def test_grid_order_property_auto_placement_005(self):
        self.assertRender('test_CssGrid1', 'grid_order_property_auto_placement_005')

    def test_grid_order_property_painting_001(self):
        self.assertRender('test_CssGrid1', 'grid_order_property_painting_001')

    def test_grid_order_property_painting_002(self):
        self.assertRender('test_CssGrid1', 'grid_order_property_painting_002')

    def test_grid_order_property_painting_003(self):
        self.assertRender('test_CssGrid1', 'grid_order_property_painting_003')

    def test_grid_order_property_painting_004(self):
        self.assertRender('test_CssGrid1', 'grid_order_property_painting_004')

    def test_grid_order_property_painting_005(self):
        self.assertRender('test_CssGrid1', 'grid_order_property_painting_005')

    def test_grid_support_display_001(self):
        self.assertRender('test_CssGrid1', 'grid_support_display_001')

    def test_grid_support_flexible_lengths_001(self):
        self.assertRender('test_CssGrid1', 'grid_support_flexible_lengths_001')

    def test_grid_support_grid_auto_columns_rows_001(self):
        self.assertRender('test_CssGrid1', 'grid_support_grid_auto_columns_rows_001')

    def test_grid_support_grid_template_areas_001(self):
        self.assertRender('test_CssGrid1', 'grid_support_grid_template_areas_001')

    def test_grid_support_grid_template_columns_rows_001(self):
        self.assertRender('test_CssGrid1', 'grid_support_grid_template_columns_rows_001')

    def test_grid_support_named_grid_lines_001(self):
        self.assertRender('test_CssGrid1', 'grid_support_named_grid_lines_001')

    def test_grid_support_repeat_001(self):
        self.assertRender('test_CssGrid1', 'grid_support_repeat_001')

    def test_grid_template_columns_rows_resolved_values_001(self):
        self.assertRender('test_CssGrid1', 'grid_template_columns_rows_resolved_values_001')

    def test_grid_vertical_align_001(self):
        self.assertRender('test_CssGrid1', 'grid_vertical_align_001')

    def test_grid_z_axis_ordering_001(self):
        self.assertRender('test_CssGrid1', 'grid_z_axis_ordering_001')

    def test_grid_z_axis_ordering_002(self):
        self.assertRender('test_CssGrid1', 'grid_z_axis_ordering_002')

    def test_grid_z_axis_ordering_003(self):
        self.assertRender('test_CssGrid1', 'grid_z_axis_ordering_003')

    def test_grid_z_axis_ordering_004(self):
        self.assertRender('test_CssGrid1', 'grid_z_axis_ordering_004')

    def test_grid_z_axis_ordering_005(self):
        self.assertRender('test_CssGrid1', 'grid_z_axis_ordering_005')

    def test_grid_z_axis_ordering_overlapped_items_001(self):
        self.assertRender('test_CssGrid1', 'grid_z_axis_ordering_overlapped_items_001')

    def test_grid_z_axis_ordering_overlapped_items_002(self):
        self.assertRender('test_CssGrid1', 'grid_z_axis_ordering_overlapped_items_002')

    def test_grid_z_axis_ordering_overlapped_items_003(self):
        self.assertRender('test_CssGrid1', 'grid_z_axis_ordering_overlapped_items_003')

    def test_grid_z_axis_ordering_overlapped_items_004(self):
        self.assertRender('test_CssGrid1', 'grid_z_axis_ordering_overlapped_items_004')

    def test_grid_z_axis_ordering_overlapped_items_005(self):
        self.assertRender('test_CssGrid1', 'grid_z_axis_ordering_overlapped_items_005')

    def test_grid_z_axis_ordering_overlapped_items_006(self):
        self.assertRender('test_CssGrid1', 'grid_z_axis_ordering_overlapped_items_006')

