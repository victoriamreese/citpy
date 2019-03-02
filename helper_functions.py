import math


def calc_length(x1, y1, x2, y2):
    """
    calculate the length of a line segment
    """
    ydif, xdif = abs(y2-y1), abs(x2-x1)
    slope = ydif/xdif
    length = math.sqrt(ydif**2 + xdif**2)
    return slope, length
    
#compare length of two line segments and return larger one
def which_bigger(line1, line2):
    return max()
    if line1>line2:
        return line1
    else:
        return line2
    
    # other option for one-line
    return line1 if line1>line2 else line2 
        
        
#see if two line segments intersect
#optional - we probably don't need this bc intersecting 
def if_intersect(line1, line2):
    pass
    #two lines, four points.
    #x1, y1 and x2, y2
    

#find angle between lines
def angle_between(slope2, slope1):
    num = (slope2 - slope1)
    denom = (1 + slope2 * slope1)
    if denom == 0:
        print(90.0)
    else:
        print(((math.atan(num/denom)*180/math.pi)))




    
