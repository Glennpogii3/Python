def python_food():
    width = 100
    text = "Happy Anniversary"
    center_text = (width - len(text)) // 2
    print(" " * center_text, text)

def center_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    center_text = (80 - len(text)) // 2
    return " " * center_text + text

# with open('centered', mode='w') as center_file:
    # Call the function
# s1 = center_text("aaa")
# print(s1)
# s2 = center_text("aaaaa")
# print(s2)
# s3 = center_text(12)
# print(s3)
# s4 = center_text("aaaaaaa")
# print(s4)
# s5 = center_text(2, 2, "Hellsd", 'assd')
# print(s5)
# print("=" + str(123 * 232))
# print(sorted(["a", "w", "d", "f"]))

with open("menu", "w") as menu:
    s1 = center_text("aaa")
    print(s1, file=menu)
    s2 = center_text("aaaaa")
    print(s2, file=menu)
    s3 = center_text(12)
    print(s3, file=menu)
    s4 = center_text("aaaaaaa")
    print(s4, file=menu)
    s5 = center_text(2, 2, "Hellsd", 'assd')
    print(s5, file=menu)
