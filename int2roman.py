def intToRoman(num) :
    d = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M', 0:''}
    values = [1, 5, 10, 50, 100, 500, 1000]
    buffer = 0
    roman = ''
    x = 0 
    max = 0
    for i in values: 
        if(num%i == 0):
            max = i
        else:
            break
    return max

print(intToRoman(3))

