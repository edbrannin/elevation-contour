class Point(object):
    def __init__(self, lat, lon, elevation=0):
        self.lat = lat
        self.lon = lon
        self.elevation = elevation

    def __eq__(self, other):
        return (self.lat == other.lat) and (self.lon == other.lon) and (
            self.elevation == other.elevation)


class Points(object):
    def __init__(self, lat1, lon1, lat2, lon2, resolution=100):
        self.min_lat = min(lat1, lat2)
        self.min_lon = min(lon1, lon2)

        self.max_lat = max(lat1, lat2)
        self.max_lon = max(lon1, lon2)

        self.resolution = resolution
        self.points = dict()

    def range(self, start, end):
        'Calculate the range of points from start to finish, with the desired resolution'
        for x in range(start * self.resolution, end * self.resolution + 1):
            yield float(x) / self.resolution

    def point(self, lat, lon):
        key = (lat, lon)
        if key not in self.points:
            self.points[key] = Point(lat, lon)
        return self.points[key]

    def all_points(self):
        for lat in self.range(self.min_lat, self.max_lat):
            for lon in self.range(self.min_lon, self.max_lon):
                yield self.point(lat, lon)
