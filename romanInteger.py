"""
    -> We need to check the roman numeral from left to right
    -> If the right word is smaller than current one subtract the value from it.
    -> Else keep adding the value
"""
"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""

#lets create a dictionary
roman_numerals = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000,
}
input = 'LVIII'
input2 = "MCMXCIV"
#we need a function to know the value of the letter
def getValue(x):
    return roman_numerals[x]

def convertToDecimal(x):
    total = 0
    for i in range(len(x) - 1):
        if getValue(x[i]) < getValue(x[i+1]):
            total = total - getValue(x[i])
        else:
            total = total + getValue(x[i])
    return total + getValue(x[-1])

print(convertToDecimal(input))
print(convertToDecimal(input2))
