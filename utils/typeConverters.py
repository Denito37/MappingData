from shapely.geometry import Point


def s_to_p(string):
    """Convert a comma-separated string to a Shapely Point.
    
    Args:
        string: Coordinate string in format "x,y" (e.g., "-73.9857,40.7484")
        
    Returns:
        Point: Shapely Point object, or None if conversion fails
        
    Example:
        >>> point = s_to_p("-73.9857,40.7484")
        >>> point.x
        -73.9857
    """
    try:
        x_str, y_str = string.split(',')
        x = float(x_str.strip())
        y = float(y_str.strip())
        return Point(x, y)
    except (ValueError, AttributeError) as e:
        print(f'Invalid string format: {string}. Error: {e}')
        return None


def p_to_s(point):
    """Convert a Shapely Point to a comma-separated string.
    
    Args:
        point: Shapely Point object
        
    Returns:
        str: Coordinate string in format "x,y", or None if conversion fails
        
    Example:
        >>> from shapely.geometry import Point
        >>> p_to_s(Point(-73.9857, 40.7484))
        '-73.9857,40.7484'
    """
    try:
        return f"{point.x},{point.y}"
    except AttributeError as e:
        print(f'Invalid Point object. Error: {e}')
        return None


def validate_coordinates(x, y, bounds=None):
    """Validate that coordinates are within expected NYC bounds.
    
    Args:
        x: Longitude value
        y: Latitude value  
        bounds: Optional dict with 'min_x', 'max_x', 'min_y', 'max_y'
                Defaults to approximate NYC bounding box
                
    Returns:
        bool: True if coordinates are valid and within bounds
    """
    if bounds is None:
        # Approximate NYC bounding box
        bounds = {
            'min_x': -74.3,  # Western edge
            'max_x': -73.7,  # Eastern edge
            'min_y': 40.5,   # Southern edge
            'max_y': 40.95   # Northern edge
        }
    
    try:
        x = float(x)
        y = float(y)
        return (bounds['min_x'] <= x <= bounds['max_x'] and 
                bounds['min_y'] <= y <= bounds['max_y'])
    except (ValueError, TypeError):
        return False