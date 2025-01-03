nums = [1,2,3]
# Step 1: Find the first decreasing element
n = len(nums)
k = n - 2
while k >= 0 and nums[k] >= nums[k + 1]:
    k -= 1

if k == -1:
    # If no such element exists, reverse the entire array
    nums.reverse()

# Step 2: Find the element to swap with nums[k]
l = n - 1
while nums[l] <= nums[k]:
    l -= 1

# Step 3: Swap nums[k] and nums[l]
nums[k], nums[l] = nums[l], nums[k]

# Step 4: Reverse the suffix
nums[k + 1:] = reversed(nums[k + 1:])

print(nums)






# brute force method -
# arr = [3,2,1]
# pointer = len(arr) - 2

# x = arr[pointer:]
# y = list(x)
# y.sort(reverse=True)

# arrCheck = list(arr)
# arrCheck.sort(reverse=True)
# if(arr==arrCheck):
#     arr.sort()
#     print(arr)
# else:
#     while(x==y and pointer>0):
#         pointer-=1
#         x = arr[pointer:]
#         y = list(x)
#         y.sort(reverse=True)

#     y.sort()
#     for i in range(len(y)):
#         if(y[i]>x[0]):
#             x[0] = y[i]
#             y.pop(i)
#             y.sort()
#             x[1:] = y[:]
#             break
#         else:
#             i+=1
#     arr[pointer:] = x[:]
#     print(arr, pointer)
# # if(pointer==0):
  
# #  print(x)
# # # print(arr[pointer:])