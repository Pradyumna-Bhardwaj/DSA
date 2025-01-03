nums1 = [9,4,9,8,4,6]
nums2 = [4,9,5]

# res = nums1 & nums2
# nums1.sort()
# nums2.sort()
# res = list(set(nums1) & set(nums2))
res = list((set(nums1) & set(nums2)))
print(res)