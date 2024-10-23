nums = [1,1,1,3,3,4,3,2,4,2]
slow = 0
fast = 0
while(True):
    slow = nums[slow]
    fast = nums[nums[fast]] 
    if(slow!=fast):
        continue
    else: 
        break
slow = 0
while(slow!=fast):
    slow = nums[slow]
    fast = nums[fast]

