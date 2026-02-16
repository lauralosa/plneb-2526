def countA(s):
    count = 0
    for l in s:
        if l == 'A' or l == 'a':
            count +=1
    print(count) 

countA("Banana")