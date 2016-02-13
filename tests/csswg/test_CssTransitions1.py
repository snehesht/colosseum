from unittest import expectedFailure
from .. utils import CSSWGTestCase

class test_CssTransitions1(CSSWGTestCase):
    def test_before_domcontentloaded_001(self):
        self.assertRender('test_CssTransitions1', 'before_domcontentloaded_001')

    def test_before_load_001(self):
        self.assertRender('test_CssTransitions1', 'before_load_001')

    def test_changing_while_transition(self):
        self.assertRender('test_CssTransitions1', 'changing_while_transition')

    def test_currentcolor_animation_001(self):
        self.assertRender('test_CssTransitions1', 'currentcolor_animation_001')

    def test_detached_container_001(self):
        self.assertRender('test_CssTransitions1', 'detached_container_001')

    def test_events_001(self):
        self.assertRender('test_CssTransitions1', 'events_001')

    def test_events_002(self):
        self.assertRender('test_CssTransitions1', 'events_002')

    def test_events_003(self):
        self.assertRender('test_CssTransitions1', 'events_003')

    def test_events_004(self):
        self.assertRender('test_CssTransitions1', 'events_004')

    def test_events_005(self):
        self.assertRender('test_CssTransitions1', 'events_005')

    def test_events_006(self):
        self.assertRender('test_CssTransitions1', 'events_006')

    def test_events_007(self):
        self.assertRender('test_CssTransitions1', 'events_007')

    def test_hidden_container_001(self):
        self.assertRender('test_CssTransitions1', 'hidden_container_001')

    def test_properties_value_001(self):
        self.assertRender('test_CssTransitions1', 'properties_value_001')

    def test_properties_value_002(self):
        self.assertRender('test_CssTransitions1', 'properties_value_002')

    def test_properties_value_003(self):
        self.assertRender('test_CssTransitions1', 'properties_value_003')

    def test_properties_value_auto_001(self):
        self.assertRender('test_CssTransitions1', 'properties_value_auto_001')

    def test_properties_value_implicit_001(self):
        self.assertRender('test_CssTransitions1', 'properties_value_implicit_001')

    def test_properties_value_inherit_001(self):
        self.assertRender('test_CssTransitions1', 'properties_value_inherit_001')

    def test_properties_value_inherit_002(self):
        self.assertRender('test_CssTransitions1', 'properties_value_inherit_002')

    def test_properties_value_inherit_003(self):
        self.assertRender('test_CssTransitions1', 'properties_value_inherit_003')

    def test_pseudo_elements_001(self):
        self.assertRender('test_CssTransitions1', 'pseudo_elements_001')

    def test_transition_001(self):
        self.assertRender('test_CssTransitions1', 'transition_001')

    def test_transition_delay_000(self):
        self.assertRender('test_CssTransitions1', 'transition_delay_000')

    def test_transition_delay_001(self):
        self.assertRender('test_CssTransitions1', 'transition_delay_001')

    def test_transition_delay_002(self):
        self.assertRender('test_CssTransitions1', 'transition_delay_002')

    def test_transition_delay_003(self):
        self.assertRender('test_CssTransitions1', 'transition_delay_003')

    def test_transition_duration_001(self):
        self.assertRender('test_CssTransitions1', 'transition_duration_001')

    def test_transition_duration_002(self):
        self.assertRender('test_CssTransitions1', 'transition_duration_002')

    def test_transition_duration_003(self):
        self.assertRender('test_CssTransitions1', 'transition_duration_003')

    def test_transition_duration_004(self):
        self.assertRender('test_CssTransitions1', 'transition_duration_004')

    def test_transition_property_001(self):
        self.assertRender('test_CssTransitions1', 'transition_property_001')

    def test_transition_property_002(self):
        self.assertRender('test_CssTransitions1', 'transition_property_002')

    def test_transition_property_003(self):
        self.assertRender('test_CssTransitions1', 'transition_property_003')

    def test_transition_property_004(self):
        self.assertRender('test_CssTransitions1', 'transition_property_004')

    def test_transition_property_005(self):
        self.assertRender('test_CssTransitions1', 'transition_property_005')

    def test_transition_property_006(self):
        self.assertRender('test_CssTransitions1', 'transition_property_006')

    def test_transition_property_007(self):
        self.assertRender('test_CssTransitions1', 'transition_property_007')

    def test_transition_property_008(self):
        self.assertRender('test_CssTransitions1', 'transition_property_008')

    def test_transition_property_009(self):
        self.assertRender('test_CssTransitions1', 'transition_property_009')

    def test_transition_property_010(self):
        self.assertRender('test_CssTransitions1', 'transition_property_010')

    def test_transition_property_011(self):
        self.assertRender('test_CssTransitions1', 'transition_property_011')

    def test_transition_property_012(self):
        self.assertRender('test_CssTransitions1', 'transition_property_012')

    def test_transition_property_013(self):
        self.assertRender('test_CssTransitions1', 'transition_property_013')

    def test_transition_property_014(self):
        self.assertRender('test_CssTransitions1', 'transition_property_014')

    def test_transition_property_015(self):
        self.assertRender('test_CssTransitions1', 'transition_property_015')

    def test_transition_property_016(self):
        self.assertRender('test_CssTransitions1', 'transition_property_016')

    def test_transition_property_017(self):
        self.assertRender('test_CssTransitions1', 'transition_property_017')

    def test_transition_property_018(self):
        self.assertRender('test_CssTransitions1', 'transition_property_018')

    def test_transition_property_019(self):
        self.assertRender('test_CssTransitions1', 'transition_property_019')

    def test_transition_property_020(self):
        self.assertRender('test_CssTransitions1', 'transition_property_020')

    def test_transition_property_021(self):
        self.assertRender('test_CssTransitions1', 'transition_property_021')

    def test_transition_property_022(self):
        self.assertRender('test_CssTransitions1', 'transition_property_022')

    def test_transition_property_023(self):
        self.assertRender('test_CssTransitions1', 'transition_property_023')

    def test_transition_property_024(self):
        self.assertRender('test_CssTransitions1', 'transition_property_024')

    def test_transition_property_025(self):
        self.assertRender('test_CssTransitions1', 'transition_property_025')

    def test_transition_property_026(self):
        self.assertRender('test_CssTransitions1', 'transition_property_026')

    def test_transition_property_027(self):
        self.assertRender('test_CssTransitions1', 'transition_property_027')

    def test_transition_property_028(self):
        self.assertRender('test_CssTransitions1', 'transition_property_028')

    def test_transition_property_029(self):
        self.assertRender('test_CssTransitions1', 'transition_property_029')

    def test_transition_property_030(self):
        self.assertRender('test_CssTransitions1', 'transition_property_030')

    def test_transition_property_031(self):
        self.assertRender('test_CssTransitions1', 'transition_property_031')

    def test_transition_property_032(self):
        self.assertRender('test_CssTransitions1', 'transition_property_032')

    def test_transition_property_033(self):
        self.assertRender('test_CssTransitions1', 'transition_property_033')

    def test_transition_property_034(self):
        self.assertRender('test_CssTransitions1', 'transition_property_034')

    def test_transition_property_035(self):
        self.assertRender('test_CssTransitions1', 'transition_property_035')

    def test_transition_property_036(self):
        self.assertRender('test_CssTransitions1', 'transition_property_036')

    def test_transition_property_037(self):
        self.assertRender('test_CssTransitions1', 'transition_property_037')

    def test_transition_property_038(self):
        self.assertRender('test_CssTransitions1', 'transition_property_038')

    def test_transition_property_039(self):
        self.assertRender('test_CssTransitions1', 'transition_property_039')

    def test_transition_property_040(self):
        self.assertRender('test_CssTransitions1', 'transition_property_040')

    def test_transition_property_041(self):
        self.assertRender('test_CssTransitions1', 'transition_property_041')

    def test_transition_property_042(self):
        self.assertRender('test_CssTransitions1', 'transition_property_042')

    def test_transition_property_043(self):
        self.assertRender('test_CssTransitions1', 'transition_property_043')

    def test_transition_property_044(self):
        self.assertRender('test_CssTransitions1', 'transition_property_044')

    def test_transition_property_045(self):
        self.assertRender('test_CssTransitions1', 'transition_property_045')

    def test_transition_test(self):
        self.assertRender('test_CssTransitions1', 'transition_test')

    def test_transition_timing_function_001(self):
        self.assertRender('test_CssTransitions1', 'transition_timing_function_001')

    def test_transition_timing_function_002(self):
        self.assertRender('test_CssTransitions1', 'transition_timing_function_002')

    def test_transition_timing_function_003(self):
        self.assertRender('test_CssTransitions1', 'transition_timing_function_003')

    def test_transition_timing_function_004(self):
        self.assertRender('test_CssTransitions1', 'transition_timing_function_004')

    def test_transition_timing_function_005(self):
        self.assertRender('test_CssTransitions1', 'transition_timing_function_005')

    def test_transition_timing_function_006(self):
        self.assertRender('test_CssTransitions1', 'transition_timing_function_006')

    def test_transition_timing_function_007(self):
        self.assertRender('test_CssTransitions1', 'transition_timing_function_007')

    def test_transition_timing_function_008(self):
        self.assertRender('test_CssTransitions1', 'transition_timing_function_008')

    def test_transition_timing_function_009(self):
        self.assertRender('test_CssTransitions1', 'transition_timing_function_009')

    def test_transition_timing_function_010(self):
        self.assertRender('test_CssTransitions1', 'transition_timing_function_010')

    def test_transition_timing_function_011(self):
        self.assertRender('test_CssTransitions1', 'transition_timing_function_011')

    def test_transition_timing_function_012(self):
        self.assertRender('test_CssTransitions1', 'transition_timing_function_012')

    def test_transition_timing_function_013(self):
        self.assertRender('test_CssTransitions1', 'transition_timing_function_013')

    def test_transitions_animatable_properties_01(self):
        self.assertRender('test_CssTransitions1', 'transitions_animatable_properties_01')

