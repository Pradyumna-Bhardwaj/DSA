num_map = {}
nums = [2,7,11,15]
target = 9
for i, num in enumerate(nums):
    complement = target - num
    if complement in num_map:
        print([num_map[complement], i])
    num_map[num] = i
print(num_map)




# nums = [2,7,11,15]
# target = 9
# x = nums.copy()

# for i in range(len(nums)):
#     x[i] = 9 - x[i]

# for i in range(len(nums)):
#     x[i] = nums[i] + x[i]

# for i in range(len(x)):
    