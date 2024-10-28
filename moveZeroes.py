nums = [0,1]

zeroPointer = 0
for i in range(len(nums)):
    if(nums[i]!=0):
        temp = nums[i]
        nums[i] = nums[zeroPointer]
        nums[zeroPointer] = temp
        zeroPointer+=1
print(nums)