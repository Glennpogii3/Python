letters = "uvghizefjxkwylanopqrbcdmst"
values = ''.join(sorted(letters)) # Sort the values alphabet

backwards = values[::-1]
print(backwards)

# create a slice that produces the characters qpo
print(values[16:13:-1])

# slice the string to produce edcba
print(values[4::-1])

# slice the string to produce the last 8 characters, in reverse order
print(values[:-9:-1])

print(values[-4:])
print(values[-1:])
print(values[:1])
print(values[0])
