import unittest
from plant_and_segment_classes import Segment, CheckLeaf

 

class TestSegment(unittest.TestCase):


    def test_point_on_screen(self):
        seg1 =[400, 400, 200, 200] 
        self.assertTrue(Segment(seg1).point_on_screen())
    
    def test_point_off_screen(self):
        seg4 = [-400, 2, 1000, 3]    
        self.assertFalse(Segment(seg4).point_on_screen())

    def test_find_line_eqation(self):
        seg1 =[400, 400, 200, 200] 
        self.assertEqual(Segment(seg1).find_line_equation(), [-200,200,0])



    def test_find_the_intersection_point_perpendicular(self):
        seg3 =[400,200,200,400]
        seg2 =[200, 200, 400, 400]
        leaf_perpendicular = CheckLeaf(seg3, seg2)
        self.assertEqual(leaf_perpendicular.find_the_intersection_point(), [])        


    def test_find_the_intersection_point_parallel(self): 
        seg1 =[400, 400, 200, 200] 
        seg2 =[200, 200, 400, 400]
        leaf_parallel = Checkleaf(seg1, seg2)
        self.assertEqual(leaf_parallel.find_the_intersection_point(), [-1000000, -1000000])





if __name__ == '__main__':
    unittest.main()

