def intToRoman(num) :
    d = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M', 0:'', 4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}
    values = [10, 50, 100, 500, 1000]
    buffer = 0
    roman = ''
    x = 0 
    max = 0
    for i in values: 
        if(num>i):
            max = x
        else:
            break
        x+=1
    print(max)
    k = max
    while(k>-1):
        buffer = num%values[k]
        if buffer == 0:
            roman = roman+d[values[k]]
        if buffer not in d:
            roman = roman+(buffer*d[1])
        else :
            roman=roman+d[buffer]
        k-=1
    return roman

print(intToRoman(51))

