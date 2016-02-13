from unittest import expectedFailure
from .. utils import CSSWGTestCase

class test_Cssom1(CSSWGTestCase):
    def test_computed_style_001(self):
        self.assertRender('test_Cssom1', 'computed_style_001')

    def test_css_style_declaration_modifications(self):
        self.assertRender('test_Cssom1', 'css_style_declaration_modifications')

    def test_cssimportrule(self):
        self.assertRender('test_Cssom1', 'cssimportrule')

    def test_cssom_cssstyledeclaration_set(self):
        self.assertRender('test_Cssom1', 'cssom_cssstyledeclaration_set')

    def test_cssom_csstext_serialize(self):
        self.assertRender('test_Cssom1', 'cssom_csstext_serialize')

    def test_cssom_setproperty_shorthand(self):
        self.assertRender('test_Cssom1', 'cssom_setproperty_shorthand')

    def test_cssstyledeclaration_csstext(self):
        self.assertRender('test_Cssom1', 'cssstyledeclaration_csstext')

    def test_cssstyledeclaration_mutability(self):
        self.assertRender('test_Cssom1', 'cssstyledeclaration_mutability')

    def test_cssstylerule(self):
        self.assertRender('test_Cssom1', 'cssstylerule')

    def test_escape(self):
        self.assertRender('test_Cssom1', 'escape')

    def test_index_001(self):
        self.assertRender('test_Cssom1', 'index_001')

    def test_index_002(self):
        self.assertRender('test_Cssom1', 'index_002')

    def test_index_003(self):
        self.assertRender('test_Cssom1', 'index_003')

    def test_inline_style_001(self):
        self.assertRender('test_Cssom1', 'inline_style_001')

    def test_interfaces(self):
        self.assertRender('test_Cssom1', 'interfaces')

    def test_matchmedia(self):
        self.assertRender('test_Cssom1', 'matchmedia')

    def test_medialist_interfaces_001(self):
        self.assertRender('test_Cssom1', 'medialist_interfaces_001')

    def test_medialist_interfaces_002(self):
        self.assertRender('test_Cssom1', 'medialist_interfaces_002')

    def test_medialist_interfaces_003(self):
        self.assertRender('test_Cssom1', 'medialist_interfaces_003')

    def test_medialist_interfaces_004(self):
        self.assertRender('test_Cssom1', 'medialist_interfaces_004')

    def test_medialist(self):
        self.assertRender('test_Cssom1', 'medialist')

    def test_selectorserialize(self):
        self.assertRender('test_Cssom1', 'selectorserialize')

    def test_shape_outside_shape_arguments_000(self):
        self.assertRender('test_Cssom1', 'shape_outside_shape_arguments_000')

    def test_shape_outside_shape_arguments_001(self):
        self.assertRender('test_Cssom1', 'shape_outside_shape_arguments_001')

    def test_shape_outside_shape_notation_000(self):
        self.assertRender('test_Cssom1', 'shape_outside_shape_notation_000')

    def test_style_sheet_interfaces_001(self):
        self.assertRender('test_Cssom1', 'style_sheet_interfaces_001')

    def test_style_sheet_interfaces_002(self):
        self.assertRender('test_Cssom1', 'style_sheet_interfaces_002')

    def test_ttwf_cssom_doc_ext_load_count(self):
        self.assertRender('test_Cssom1', 'ttwf_cssom_doc_ext_load_count')

    def test_ttwf_cssom_doc_ext_load_tree_order(self):
        self.assertRender('test_Cssom1', 'ttwf_cssom_doc_ext_load_tree_order')

    def test_ttwf_cssom_document_extension(self):
        self.assertRender('test_Cssom1', 'ttwf_cssom_document_extension')

