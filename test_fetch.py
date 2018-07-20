from fetch import Points, Point


def test_range_0_1_10():
    points = Points(0, 0, 1, 1, resolution=10)
    result = list(points.range(0, 1))
    assert result == [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]


def test_range_33_36_1():
    points = Points(0, 0, 1, 1, resolution=1)
    result = list(points.range(33, 36))
    assert result == [33, 34, 35, 36]


def test_range_33_36_2():
    points = Points(0, 0, 1, 1, resolution=2)
    result = list(points.range(33, 36))
    assert result == [33, 33.5, 34, 34.5, 35, 35.5, 36]


def test_points_0_1_2():
    points = Points(0, 0, 1, 1, resolution=2)
    result = list(points.all_points())
    assert Point(0, 0) in result
    assert Point(1, 1) in result
