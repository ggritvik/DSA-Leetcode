nums1 = [1,2,2,1]
nums2 = [2,2]

hash_set = set()

for i in nums1:
    if i in nums2:
        hash_set.add(i)


print(list(hash_set)) 