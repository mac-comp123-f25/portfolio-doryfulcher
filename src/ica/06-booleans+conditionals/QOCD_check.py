def has_QOCD(input_string: str) -> bool:
    for char in input_string:
        if char in "QOCD":
            return True
    return False

if __name__ == "__main__":
  assert has_QOCD("Quick") == True
  assert has_QOCD("Odd") == True
  assert has_QOCD("MAC") == True
  assert has_QOCD("WiLD") == True
  assert has_QOCD("MATH") == False
  assert has_QOCD("comp123") == False
  print("All tests passed!")
