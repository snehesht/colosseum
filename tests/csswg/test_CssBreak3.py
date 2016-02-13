from unittest import expectedFailure
from .. utils import CSSWGTestCase

class test_CssBreak3(CSSWGTestCase):
    def test_floats_clear_breaks_002(self):
        self.assertRender('test_CssBreak3', 'floats_clear_breaks_002')

    def test_floats_in_named_flow_012(self):
        self.assertRender('test_CssBreak3', 'floats_in_named_flow_012')

    def test_floats_in_named_flow_029(self):
        self.assertRender('test_CssBreak3', 'floats_in_named_flow_029')

    def test_floats_in_named_flow_030(self):
        self.assertRender('test_CssBreak3', 'floats_in_named_flow_030')

    def test_position_relative_001(self):
        self.assertRender('test_CssBreak3', 'position_relative_001')

    def test_regions_transforms_008(self):
        self.assertRender('test_CssBreak3', 'regions_transforms_008')

    def test_regions_transforms_009(self):
        self.assertRender('test_CssBreak3', 'regions_transforms_009')

    def test_regions_transforms_013(self):
        self.assertRender('test_CssBreak3', 'regions_transforms_013')

    def test_regions_transforms_020(self):
        self.assertRender('test_CssBreak3', 'regions_transforms_020')

    def test_regions_transforms_021(self):
        self.assertRender('test_CssBreak3', 'regions_transforms_021')

    def test_regions_transforms_022(self):
        self.assertRender('test_CssBreak3', 'regions_transforms_022')

