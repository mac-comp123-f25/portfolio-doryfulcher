def count_negatives(numbers):
    if not numbers:
        return 0
    else:
        first_element=numbers[0]
        rest=numbers[1:]

        if first_element < 0:
            return 1+ count_negatives(rest)
        else:
            return count_negatives(rest)