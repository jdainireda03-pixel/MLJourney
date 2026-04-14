def histogram(string: str) -> dict[str, str]:
    histo = {}
    for letter in string:
        if letter not in histo:
            histo[letter] = ""
        histo[letter] += "*"

    return histo


h = histogram("statistically")

for key, value in h.items():
    print(key, value)
