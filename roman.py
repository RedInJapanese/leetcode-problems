def romanToInt(s):
    i = len(s)
    sum = 0
    checker = 1000000


    while(i>0):
        if(s[i-1] == 'I'):
            sum+=1
        if(s[i-1] == 'V'):
            sum+=5
        if(s[i-1] == 'X'):
            sum+=10
        if(s[i-1] == 'L'):
            sum+=50
        if(s[i-1] == 'C'):
            sum+=100
        if(s[i-1] == 'D'):
            sum+=500
        if(s[i-1] == 'M'):
            sum+=1000
        i-=1
    return sum

print("sum :",romanToInt("III"))