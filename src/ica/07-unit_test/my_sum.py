def sum3(values):
    assert type(values) in [list, tuple], "The values should be a list or tuple."""
    assert len(values) >= 3, "The list has at least 3 elements."
    assert type(values[0]) in [int, float], "The first value should be an int or float."
    assert type(values[1]) in [int, float], "The second value should be an int or float."
    assert type(values[2]) in [int, float], "The third value should be an int or float."

    return sum(values)

if __name__ == "__main__":
  print( sum3([5, 2, 8, -2, 6, 15]) )
  print( sum3([5, 2]) )
  print( sum3([]) )
  print( sum3(5) )
  print( sum3(["h", "i", 1, 2, 3]) )
  print( sum3([1, 2, 3, "h", "i"]) )
