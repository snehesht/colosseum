from unittest import expectedFailure
from .. utils import CSSWGTestCase

class test_Geometry1(CSSWGTestCase):
    def test_dommatrix_001(self):
        self.assertRender('test_Geometry1', 'dommatrix_001')

    def test_dompoint_001(self):
        self.assertRender('test_Geometry1', 'dompoint_001')

    def test_domquad_001(self):
        self.assertRender('test_Geometry1', 'domquad_001')

    def test_domrect_001(self):
        self.assertRender('test_Geometry1', 'domrect_001')

