import math

line1 = [3,2]
line2 = [6,7]

#calculate the length of a line segment

    

def return_major_axis(line1, line2):
    return max(line1, line2)
        





class Leaf:
    def __init__(self, x1_a, y1_a, x2_a, y2_a, x1_b, y1_b, x2_b, y2_b):
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
    
    def calc_lengths(self):
        import math
        length = math.sqrt(ydif**2 + xdif**2)
        return length_axis1, length_axis2
        

leaf = Leaf(0,0,0,0,0,0,0,0)
leaf.calc_angle_between_segments()
        


    