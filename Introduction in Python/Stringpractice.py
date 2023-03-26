s1 = "America"
s2 = "Japan"
print("Original String is", s1)
print("Original String is", s2)
res = s1[0]
res2 = s2[0]
ss1 = len(s1)
ss2 = len(s2)

mi2 = int(ss2 / 2)
mi = int(ss1 / 2)
res = res + res2 + s1[mi]
res = res + res2 + s2[mi2 + 1]





print("New String:", res)
print()


def mix_string(s1, s2):
    # get first character from both string
    first_char = s1[0] + s2[0]

    # get middle character from both string
    middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]

    # get last character from both string
    last_char = s1[len(s1) - 1] + s2[len(s2) - 1]

    # add all
    res = first_char + middle_char + last_char
    print("Mix String is ", res)
    print(middle_char)

s1 = "America"
s2 = "Japan"
mix_string(s1, s2)