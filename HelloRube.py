# Overly complicated Hello World
asciiChars = [72,101,108,108,111,32,87,111,114,108,100,33]
hello, i = "", 0
while i < len(asciiChars):
    hello += chr(asciiChars[i])
    i += 1
print(hello)
