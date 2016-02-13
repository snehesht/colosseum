from unittest import expectedFailure
from .. utils import CSSWGTestCase

class test_CssomView1(CSSWGTestCase):
    def test_caretposition_001(self):
        self.assertRender('test_CssomView1', 'caretposition_001')

    def test_cssom_getboundingclientrect_001(self):
        self.assertRender('test_CssomView1', 'cssom_getboundingclientrect_001')

    def test_cssom_getboundingclientrect_002(self):
        self.assertRender('test_CssomView1', 'cssom_getboundingclientrect_002')

    def test_cssom_getclientrects(self):
        self.assertRender('test_CssomView1', 'cssom_getclientrects')

    def test_cssom_view_window_screen_interface(self):
        self.assertRender('test_CssomView1', 'cssom_view_window_screen_interface')

    def test_elementfrompoint_001(self):
        self.assertRender('test_CssomView1', 'elementfrompoint_001')

    def test_elementfromposition(self):
        self.assertRender('test_CssomView1', 'elementfromposition')

    def test_htmlelement_offset_width_001(self):
        self.assertRender('test_CssomView1', 'htmlelement_offset_width_001')

    def test_matchmedia(self):
        self.assertRender('test_CssomView1', 'matchmedia')

    def test_matchmediaaddlistener(self):
        self.assertRender('test_CssomView1', 'matchmediaaddlistener')

    def test_media_query_list_interface(self):
        self.assertRender('test_CssomView1', 'media_query_list_interface')

    def test_mediaquerylist_001(self):
        self.assertRender('test_CssomView1', 'mediaquerylist_001')

    def test_offsetparent_element_test(self):
        self.assertRender('test_CssomView1', 'offsetparent_element_test')

    def test_screen_pixeldepth_screen_colordepth001(self):
        self.assertRender('test_CssomView1', 'screen_pixeldepth_screen_colordepth001')

    def test_scrollwidthheight(self):
        self.assertRender('test_CssomView1', 'scrollwidthheight')

    def test_scrollwidthheightwhennotscrollable(self):
        self.assertRender('test_CssomView1', 'scrollwidthheightwhennotscrollable')

    def test_ttwf_scrollintoview(self):
        self.assertRender('test_CssomView1', 'ttwf_scrollintoview')

    def test_window_interface(self):
        self.assertRender('test_CssomView1', 'window_interface')

    def test_window_screen_height_immutable(self):
        self.assertRender('test_CssomView1', 'window_screen_height_immutable')

    def test_window_screen_height_mutation_throws(self):
        self.assertRender('test_CssomView1', 'window_screen_height_mutation_throws')

    def test_window_screen_height(self):
        self.assertRender('test_CssomView1', 'window_screen_height')

    def test_window_screen_width_immutable(self):
        self.assertRender('test_CssomView1', 'window_screen_width_immutable')

    def test_window_screen_width_mutation_throws(self):
        self.assertRender('test_CssomView1', 'window_screen_width_mutation_throws')

    def test_window_screen_width(self):
        self.assertRender('test_CssomView1', 'window_screen_width')

