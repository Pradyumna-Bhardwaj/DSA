nums = [1,2,3,10,4]
# read Kadane's Algo for better understanding
res = nums[0]
maxPreviousSum = 0
startIndex = 0
endIndex = len(nums) - 1
for i in range(len(nums)):
    maxPreviousSum = maxPreviousSum + nums[i]
    if(maxPreviousSum < nums[i]):
        startIndex = i
        maxPreviousSum = nums[i]
    if(maxPreviousSum>res):
        res = maxPreviousSum
        endIndex = i
    # print(maxPreviousSum, res)
print(res, nums[startIndex:endIndex+1])