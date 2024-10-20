nums1 = [0, 0, 0]
m = 0
nums2 = [4, 28, 22]
n = 3

i=m
if(m==0):
    for j in range(len(nums2)):
        nums1[j] = nums2[j]
    # nums1.sort()
# if(n==0):
#     nums1.sort()

while(i<m+n and m!=0 and n!=0):
    nums1[i] = nums2[i-m]
    i+=1
nums1.sort()

print(nums1)