def romanToInt(s):
    d = {1: "I", 4:"IV",5:"V",9:"IX",10:"X", 40:"XL",50:"L",
        90:"XC",
        100:"C",
        400:"CD",
        500:"D",
        900:"CM",
        1000:"M"}
    roman = ''
    for i in sorted(d, reverse=True):
        if num//i:
            roman+=d[i]*(num//i)
            num-=(i*(num//i))
    return roman
    
print("sum :",romanToInt("IV"))