def up_to_period(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
    accumulator = ""
    for char in text:
        accumulator += char
        if char == '.':
            break
    return accumulator

