def romanToInt(s):
    i = len(s)
    buffer = ''
    check = 'P'
    sum = 0
    d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'P':0}
    
    while(i>0):
        buffer = s[i-1]
        if(d[check]>d[buffer]):
            sum-=d[buffer]
        else: 
            sum+=d[buffer]
        i-=1
        check = buffer
    return sum

print("sum :",romanToInt("IV"))