def number_of_steps(num):
    count: int = 0

    while num != 0:
        if num % 2 == 0:
            num = num // 2
            count = count + 1

        if num % 2 == 1:
            num = num - 1
            count = count + 1

    return count

rev = number_of_steps(14)
print(rev)

"""
step 1 : intializing the counter
step 2 : enter the loop condition: till the number is not equal to 0
step 3 : check if the number is even
    if even then update  the num = num / 2
    increment the counter
step 4 : check if the number is odd
    if odd then update the num = num - 1
    increment the counter
step 5 : return counter
"""

