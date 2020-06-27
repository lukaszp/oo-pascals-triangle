from .pascals_triangle_math import PascalsTriangleMath

class OptimizedPascalsTriangle(PascalsTriangleMath):
    
    def __init__(self):
        self.triangle_values_mem = {}
    
    def optimized_value_in(self, coordinates, ignored_next_iteration_function = None):

        coordinates = self.cast_mirrored_columns(coordinates)
            
        try:
            return self.triangle_values_mem[coordinates]
        except KeyError:
            self.triangle_values_mem[coordinates] = self.value_in(coordinates, self.optimized_value_in)
            return self.triangle_values_mem[coordinates]