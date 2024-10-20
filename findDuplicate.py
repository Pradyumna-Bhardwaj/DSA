nums = [3,1,3,4,5,2]
slow = 0
fast = 0
i = 0
while(True):
    slow = nums[slow]
    fast = nums[nums[fast]] 
    if(slow!=fast):
        continue
    else: 
        break
print(slow)
slow = 0
while(slow!=fast):
    slow = nums[slow]
    fast = nums[fast]
print(fast)