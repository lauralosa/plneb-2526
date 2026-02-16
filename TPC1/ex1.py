def reverse_string(s):
    reversedstring=""
    for l in s[::-1]:
        reversedstring += l
    print(reversedstring)

reverse_string("Banana")