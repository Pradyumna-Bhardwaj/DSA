nums = [1,1,2]

k = len(nums)
for i in range(len(nums)-1):
    if (nums[i] == nums[i+1]):
        nums[i] = 101
        k-=1
nums.sort()
print(nums, k)