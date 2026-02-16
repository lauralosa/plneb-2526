def isAnagrama(s1,s2):
    lista1=[]
    lista2=[]
    for l in s1:
        lista1.append(l)
    for l in s2:
        lista2.append(l)
    lista1.sort()
    lista2.sort()
    if lista1==lista2:
        return True
    else:
        return False


print(isAnagrama("listen","silent"))
print(isAnagrama("hello", "world"))
