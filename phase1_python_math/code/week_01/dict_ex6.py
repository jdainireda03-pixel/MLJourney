def invert(dictionary: dict):
    inverse = {value: key for key, value in dictionary.items()}
    dictionary.clear()
    dictionary.update(inverse)


s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
invert(s)
print(s)
