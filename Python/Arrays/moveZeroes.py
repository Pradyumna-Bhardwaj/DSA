nums = [0,0,1,1,0,3,12]

zeroPointer = 0
for i in range(len(nums)):
    if(nums[i]!=0):
        temp = nums[i]
        nums[i] = nums[zeroPointer]
        nums[zeroPointer] = temp
        zeroPointer+=1
print(nums)