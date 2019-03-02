import math


class Leaf:
    def __init__(self, x1_a, y1_a, x2_a, y2_a, x1_b, y1_b, x2_b, y2_b):
        self.x1_a = x1_a
        self.y1_a = y1_a
        self.x2_a = x2_a
        self.y2_a = y2_a
        self.x1_b = x1_b
        self.y1_b = y1_b
        self.x2_b = x2_b
        self.y2_b = y2_b
        self.axis1 = [(x1_a, y1_a),(x2_a, y2_a)]
        self.axis2 = [(x1_b, y1_b), (x2_b, y2_b)]
        self.slope1 = abs(y1_a - y2_a)/abs(x1_a - x2_a) if abs(x1_a - x2_a) != 0 else 0.0
        self.slope2 = abs(y1_b - y2_b)/abs(x1_b - x2_b) if abs(x1_b - x2_b) != 0 else 0.0       

    def calc_angle_between_segments(self):
        numerator = (self.slope2 - self.slope1)
        denominator = (1 + self.slope2 * self.slope1)
        if denominator == 0:
            return 90.0
        else:
            return ((math.atan(numerator/denominator)*180/math.pi))
    
    def calc_lengths_major_minor(self):
        """
        returns length of axes in order of size, 
        [minor axis, major axis]
        """
        import math
        length_axis1 = math.sqrt(abs(self.y1_a - self.y2_a)**2 + abs(self.x1_a - self.x2_a)**2)
        length_axis2 = math.sqrt(abs(self.y1_b - self.y2_b)**2 + abs(self.x1_b - self.x2_b)**2)
        return sorted([length_axis1, length_axis2])
    
    def check_intersection(self):
        #todo
        pass
        
    
        

leaf = Leaf(3,2,5,4,7,6,6,6)
leaf.calc_lengths_major_minor()

        


    