from sys import stdin

while 1:
    sentence = stdin.readline().strip()

    if sentence in "EOI":
        break

    if "nemo" in sentence.lower():
        print("Found")
    else:
        print("Missing")

