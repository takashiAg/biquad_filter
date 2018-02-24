# -*- coding: utf-8 -*-

from .context import biquad_filter

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test1(self):
        biquad=biquad_filter.biquad()
        biquad.init_value()
        self.assertEqual(biquad.input_1,0)
        self.assertEqual(biquad.input_2,0)
        self.assertEqual(biquad.output_0,0)
        self.assertEqual(biquad.output_1,0)
        self.assertEqual(biquad.output_2,0)




if __name__ == '__main__':
    unittest.main()