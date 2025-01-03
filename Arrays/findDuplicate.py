nums = [1,2,3,4,1]
slow = 0
fast = 0
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

print("slow = ", slow, "\nfast = ", fast)