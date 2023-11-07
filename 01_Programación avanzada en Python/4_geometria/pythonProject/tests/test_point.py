from geom2d import Point, Vector
import pytest
import math


@pytest.mark.parametrize("a, b, expected", [
    (Point(1, 1), Point(2, 2), math.sqrt(1))])
def test_distance(a, b, expected):
    assert a.distance(b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (Point(2, 2), Point(2.000, 2.000), True)])
def test_hash(a, b, expected):
    assert (hash(a) == hash(b)) == expected


@pytest.mark.parametrize("a, b, expected", [
    (Point(2, 2), Vector(2,2), False)])
def test_hash2(a, b, expected):
    assert (hash(a) == hash(b)) == expected
