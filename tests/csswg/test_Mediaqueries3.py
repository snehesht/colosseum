from unittest import expectedFailure
from .. utils import CSSWGTestCase

class test_Mediaqueries3(CSSWGTestCase):
    def test_aspect_ratio_001(self):
        self.assertRender('test_Mediaqueries3', 'aspect_ratio_001')

    def test_aspect_ratio_002(self):
        self.assertRender('test_Mediaqueries3', 'aspect_ratio_002')

    def test_aspect_ratio_003(self):
        self.assertRender('test_Mediaqueries3', 'aspect_ratio_003')

    def test_aspect_ratio_004(self):
        self.assertRender('test_Mediaqueries3', 'aspect_ratio_004')

    def test_calc_in_media_queries_001(self):
        self.assertRender('test_Mediaqueries3', 'calc_in_media_queries_001')

    def test_calc_in_media_queries_002(self):
        self.assertRender('test_Mediaqueries3', 'calc_in_media_queries_002')

    def test_device_aspect_ratio_001(self):
        self.assertRender('test_Mediaqueries3', 'device_aspect_ratio_001')

    def test_device_aspect_ratio_002(self):
        self.assertRender('test_Mediaqueries3', 'device_aspect_ratio_002')

    def test_device_aspect_ratio_003(self):
        self.assertRender('test_Mediaqueries3', 'device_aspect_ratio_003')

    def test_device_aspect_ratio_004(self):
        self.assertRender('test_Mediaqueries3', 'device_aspect_ratio_004')

    def test_device_aspect_ratio_005(self):
        self.assertRender('test_Mediaqueries3', 'device_aspect_ratio_005')

    def test_device_aspect_ratio_006(self):
        self.assertRender('test_Mediaqueries3', 'device_aspect_ratio_006')

    def test_min_width_001(self):
        self.assertRender('test_Mediaqueries3', 'min_width_001')

    def test_min_width_tables_001(self):
        self.assertRender('test_Mediaqueries3', 'min_width_tables_001')

    def test_mq_calc_002(self):
        self.assertRender('test_Mediaqueries3', 'mq_calc_002')

    def test_mq_calc_003(self):
        self.assertRender('test_Mediaqueries3', 'mq_calc_003')

    def test_mq_calc_004(self):
        self.assertRender('test_Mediaqueries3', 'mq_calc_004')

    def test_mq_calc_005(self):
        self.assertRender('test_Mediaqueries3', 'mq_calc_005')

