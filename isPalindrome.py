#we define the function to compare
def isPalindrom(palindrome:list):
    reversed = palindrome[::-1]
    print(reversed)
    if palindrome == reversed:
        return True 
    else:
        return False

        
#define a function to extract the digits from the number
def digitExtract(num):
    digitList = list()
    if num < 0:
        digitList.append('-')
        num = abs(num)
    for i in range(len(str(num))):
        new = num // 10
        digit = num - new * 10
        digitList.append(digit)
        num = num // 10

    print(digitList)
    return isPalindrom(digitList)

#we need to test the function
input1 = 1234
input2 = -1234
input3 = 121
print(digitExtract(input1))
print(digitExtract(input2))

print(digitExtract(input3))
