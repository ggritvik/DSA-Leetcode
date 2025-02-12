nums = [100,4,200,1,3,2]

hash_set = set(nums)
longest = 0
for num in nums:
    if num-1 not in hash_set:
        length = 1
        while num+ length in hash_set:
            length += 1
        longest = max(longest, length)

print(longest)
