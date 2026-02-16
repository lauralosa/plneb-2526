def countOcurrences(s1,s2):
    count = 0
    for i in range(len(s2)-len(s1)+1):
        if s2[i:i+len(s1)] == s1:
            count += 1
    return count

print(countOcurrences("ana", "mariana"))
print(countOcurrences("na", "banana"))