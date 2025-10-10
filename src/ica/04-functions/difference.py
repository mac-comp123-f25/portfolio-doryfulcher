def smallest_diff(x, y, z):
    assert type(x) == int and type(y) == int and type(z) == int
    diff1 = abs(x - y)
    diff2 = abs(y - z)
    diff3 = abs(x - z)
    min_diff = min(diff1, diff2, diff3)
    print(diff1, diff2, diff3, 'return value:', min_diff)
    return min_diff

smallest_diff(3, 9, 5)
print(smallest_diff(3, 9, 5))