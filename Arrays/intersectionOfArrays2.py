# Moderate space and time complexity
from collections import Counter
    
# Find the intersection of two counters
counts = Counter(nums1) & Counter(nums2)

# Expand the counts into a list
result = []
for num, count in counts.items():
    result.extend([num] * count)

print(result)


# hashmap method but space complexity is high [Best time complexity]
# from collections import Counter

# nums1 = [1,2,2,1] 
# nums2 = [2,2]
# # Count elements in the first array
# counts = Counter(nums1)
# result = []

# # Iterate through the second array
# for num in nums2:
#     if counts[num] > 0:  # If num exists in nums1
#         result.append(num)
#         counts[num] -= 1  # Decrease count in hashmap
        
# print(counts)



# nums1 = [1,2,2,1] 
# nums2 = [2,2]

# map1 = [0]*1001
# map2 = [0]*1001
# map3 = [0]*1001
# output = []

# for i in nums1:
#     map1[i]+=1
# for i in nums2:
#     map2[i]+=1

# for i in range(len(map1)):
#     if(map1[i] != 0):
#         map3[i] = min(map1[i], map2[i])

# for i in range(len(map3)):
#     output.extend([i]*map3[i])

# print(output)

