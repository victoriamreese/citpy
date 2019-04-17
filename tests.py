import cleaning_functions
import unittest

 
segment = Segment(2,3,5,4)

class MyTests(unittest):

seg1 = Segment(400, 400, 200, 200) 
seg2 = Segment(200, 200, 400, 400)
print(seg1.find_line_equation())
print(seg2.find_line_equation())
# that combo is parallel ...> assertEqual([-1000000, -1000000]) 
leaf = CheckLeaf([400,200,200,400], [200,200,400,400])
print(leaf.find_the_intersection_point())

print(segment)
