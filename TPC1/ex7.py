def balancedString(s1, s2):
    for l in s1:
        if l not in s2:
            return False
    return True

print(balancedString("ana", "mariana"))
print(balancedString("mariana", "ana"))


