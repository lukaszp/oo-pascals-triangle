import unittest
from hypothesis import given
from hypothesis.strategies import integers

from pascals_triangle import *


class TestPascalTriangle(unittest.TestCase):
    def test_value_in_on_top_part(self):
        p_t = PascalsTriangleMath() 
        self.assertEqual(p_t.value_in((0, 0), p_t.value_in), 1)
        self.assertEqual(p_t.value_in((2, 1), p_t.value_in), 2)
        self.assertEqual(p_t.value_in((4, 1), p_t.value_in), 4)
        self.assertEqual(p_t.value_in((4, 2), p_t.value_in), 6)
        self.assertEqual(p_t.value_in((4, 3), p_t.value_in), 4)
    
    @given(integers(min_value = 0))
    def test_value_in_on_left_border(self, row):
        p_t = PascalsTriangleMath()
        self.assertEqual(p_t.value_in((row, 0), p_t.value_in), 1)
        
class TestOptimizedPascalsTriangle(unittest.TestCase):
    
    
    def test_optimized_value_in_on_top(self):
        p_t = OptimizedPascalsTriangle()
        self.assertEqual(p_t.optimized_value_in((0, 0)), 1)
        self.assertEqual(p_t.optimized_value_in((2, 1)), 2)
        self.assertEqual(p_t.optimized_value_in((4, 1)), 4)
        self.assertEqual(p_t.optimized_value_in((4, 2)), 6)
        self.assertEqual(p_t.optimized_value_in((4, 3)), 4)
        
    def test_not_caching_border_mirrored(self):
        p_t = OptimizedPascalsTriangle()
        self.assertEqual(p_t.optimized_value_in((4, 1)), 4)
        self.assertEqual(p_t.optimized_value_in((4, 2)), 6)
        self.assertEqual(p_t.optimized_value_in((4, 3)), 4)
        with self.assertRaises(KeyError) as context:
            p_t.triangle_values_mem[(3, 2)]
            p_t.triangle_values_mem[(4, 3)]
        

unittest.main(exit=False)
