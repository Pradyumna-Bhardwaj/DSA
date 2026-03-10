nums = [1]
k = 3
# for i in range(0,k):
#     storeVar = nums[len(nums)-1]
#     nums.pop(len(nums)-1)
#     nums.insert(0,storeVar)
# print(nums)

# code for reversing
def reversal(nums, start, end):
    while(start<=end):
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start+=1
        end-=1
k = k%len(nums)
reversal(nums, 0, len(nums)-1)
reversal(nums, 0, k-1)
reversal(nums, k, len(nums)-1)
print(nums)


