from shapely.geometry import Point

# converts string to Geo Point
def s_to_p(string):
    try:
        x_str, y_str = string.split(',')
        x = float(x_str)
        y = float(y_str)
        coord = Point(x,y)
    except ValueError:
        print('Invalid string format')
    return coord