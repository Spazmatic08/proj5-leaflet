"""
Creates a dict of string: tuples that indicates the title and lat/lng
coordinates of somewhere. 
"""

class POI():
    """
    A dict of POI coordinates.
    Can be instantiated with a file or a list of strings.
    """
    
    def __init__(self, points):
        """
        Initialize with the provided POIs.
        Args:
            points: a file, path to a file, or a list of strings.
            Each POI occurs on one line, in the format Name/lat/lng.
            Empty lines and lines beginning with # are treated as
            comments.
        Returns: nothing
        Effect: the new POI object containing the series of POIs
        Raises: IOError if points is a bad path
        """
        self.points = {}
        if isinstance(points, str):
            ps = open(points, 'r')
        else:
            ps = points

        for point in ps:
            point = point.strip()
            if len(point) == 0 or point.startswith('#'):
                continue
            point = point.split('/')
            self.points[point[0]] = [float(point[1]), float(point[2])]
