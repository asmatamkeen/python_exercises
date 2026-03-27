import math
def no_of_cans(height, width):
    area=height*width
    coverage=7
    if area<=7:
        cans=1
    else:
        cans=area/coverage

    
    
    print(f"No of cans required to paint a wall with height {height} and width {width} is {math.ceil(cans)}")

h=int(input("Enter the height of the wall(in m):"))
b=int(input("Enter the width of the wall(in m):"))

no_of_cans(h,b)