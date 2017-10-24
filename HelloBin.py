# Converts each letter to its binary representation
hello = "Hello World"
for letter in hello:
    print(letter, bin(ord(letter))[2:].zfill(8))
