import unittest
from src.reversal_operators import *

class ReversalTests(unittest.TestCase):
    def test_restore_targets_checkpoint(self):
        s=State(9);c=State(3);t=restore(s,c)
        self.assertEqual(t.after,c);self.assertTrue(t.information_lost)

    def test_reset_is_not_restore_to_arbitrary_checkpoint(self):
        s=State(9);initial=State(0);checkpoint=State(3)
        self.assertNotEqual(reset(s,initial).after,restore(s,checkpoint).after)

    def test_cancel_numeric_is_algebraic_zero(self):
        self.assertEqual(cancel_numeric(7),0)

    def test_delete_is_logical_marker(self):
        t=logical_delete(State("secret"))
        self.assertEqual(t.after.phase,Phase.DELETED);self.assertIsNone(t.after.value)

    def test_hold_is_identity_transition(self):
        s=State(4);t=hold(s)
        self.assertEqual(t.before,t.after);self.assertFalse(t.information_lost)

    def test_preinit_required_for_initialize(self):
        p=preinitialize();self.assertEqual(initialize(p,0).after.phase,Phase.INIT)
        with self.assertRaises(ValueError):initialize(State(1),0)

if __name__=="__main__":unittest.main()
