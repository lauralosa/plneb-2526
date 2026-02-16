def isCapicua(s):
    invertedstring=''
    for i in range(len(s)-1,-1,-1):
        invertedstring+=s[i]
    if invertedstring==s:
        return True
    else:
        return False

print(isCapicua('2002'))
print(isCapicua('ana'))
print(isCapicua('banana'))

