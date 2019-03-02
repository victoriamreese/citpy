import math

#calculate the length of a line segment
def calc_length(x1, y1, x2, y2):
    import math
    ydif, xdif = abs(y2-y1), abs(x2-x1)
    slope = ydif/xdif
    length = math.sqrt(ydif**2 + xdif**2)
    return length, slope
    

def return_major_axis(line1, line2):
    return max(line1, line2)
        
def check_if_lines_intersect(line1, line2):
    pass
    #two lines, four points.
    #x1, y1 and x2, y2
    


def calc_angle_between_segments(slope2, slope1):
    numerator = (slope2 - slope1)
    denomianator = (1 + slope2*slope1)
    if denom == 0:
        print(90.0)
    else:
        print(((math.atan(num/denom)*180/math.pi)))




    