import math
from typing import List, Any


class Segment(Object):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def find_line_equations(self,x1,x2,y1,y2):
        A = y1 - y2
        B = x2 - x1
        C = A*x1 + B*y1
        return_list: List[Any] = [A,B,C]
        return return_list


testseg = Segment(3, 4, 5, 6)
print(testseg.y1)


class CheckLeaf(Leaf):
     def __init__(self, [x1_a, y1_a, x2_a, y2_a], [x1_b, y1_b, x2_b, y2_b]):
        self.x1_a = x1_a
        self.y1_a = y1_a
        self.x2_a = x2_a
        self.y2_a = y2_a
        self.x1_b = x1_b
        self.y1_b = y1_b
        self.x2_b = x2_b
        self.y2_b = y2_b
        self.segA = Segment(x1_a, y1_a)
        self.axis1 = [(x1_a, y1_a),(x2_a, y2_a)]
        self.axis2 = [(x1_b, y1_b), (x2_b, y2_b)]
        self.slope_a = abs(y1_a - y2_a)/abs(x1_a - x2_a) if abs(x1_a - x2_a) != 0 else 0.0
        self.slope_b = abs(y1_b - y2_b)/abs(x1_b - x2_b) if abs(x1_b - x2_b) != 0 else 0.0       

     def find_the_intersection_point (self, list_1, list_2):
        coefficient_matrix = np.matrix([[list_1[0], list_1[1]],[list_2[0],list_2[1]]])
        RHS_matrix = np.matrix([[list_1[2]],[list_2[2]]])
        #print(coefficient_matrix) debugging code
        det = np.linalg.det(coefficient_matrix)
        #debugging code print(det)
        if(det**2 > 0.00000001) :
            #in this case, the segments intersect somewhere
            inverse_coefficient_matrix = coefficient_matrix.I
            solution = inverse_coefficient_matrix.dot(RHS_matrix)
            return(solution)
        else:
            #in this case, the lines are essentially parallel, so they will not intersect on screen, if at all.  I've put in a fake point which will fail a later llogic check.
            return([-1000000,-1000000])

    #This uses the previous two functions to give back a specific answer as to whether the two
    #line segments intersect (knowing their endpoint coordinates).
    def line_segments_intersect(x1_a,x2_a,y1_a,y2_a,x1_b,x2_b,y1_b,y2_b):
      a_coefficients = find_line_equation(ax1,ax2,ay1,ay2) #reference the earlier function
      b_coefficients = find_line_equation(bx1,bx2,by1,by2) #reference the earlier function
      det = np.linalg.det(np.matrix([[a_coefficients[0], a_coefficients[1]],[b_coefficients[0],b_coefficients[1]]]))
      print(det)
      if (det**2 > 0.0001) :
          print(det)
          intersection_point = find_the_intersection_point(a_coefficients, b_coefficients) #reference the earlier function
          #Now find the boundaries of the line segments. 
          min_ax = int(min(ax1,ax2)); max_ax = int(max(ax1,ax2))
          min_ay = int(min(ay1,ay2)); max_ay = int(max(ay1,ay2))
          min_bx = int(min(bx1,bx2)); max_bx = int(max(bx1,bx2))
          min_by = int(min(by1,by2)); max_by = int(max(by1,by2))
          #If the intersection is within the boundaries
          #defined by the most extreme values of the coordinates then we can be assured that the
          #line segments actually do intersect. The following if statement returns the necessary 
          #TRUE or FALSE that we want to see in order to move on.
          if ((min_ax <= intersection_point[0] <= max_ax) and \
              (min_ay <= intersection_point[1] <= max_ay) and \
              (min_bx <= intersection_point[0] <= max_bx) and \
              (min_by <= intersection_point[1] <= max_by)):
              return(True)
          else:
              return(False)
      else:
          return(False)
          #a determinent of zero means the line segments are parallel. 

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

        


    
