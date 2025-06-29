nums = [2,7,11,14]
target = 9
def twoSum(nums, target):
        num_map = {}  # Hash table to store number and its index

        for i, num in enumerate(nums):
            complement = target - num  # Find the complement
            print("complement", complement)
            if complement in num_map:
                return [num_map[complement], i]  # Return indices of complement and current number
                print([num_map[complement],i])
            num_map[num] = i  # Store the number with its index
            print(num_map)

res = twoSum(nums, target)
print(res)
