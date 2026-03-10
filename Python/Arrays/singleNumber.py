nums = [4,1,2,1,2]

xor = 0
for i in range(len(nums)):
    xor = xor ^ nums[i]
print(xor)