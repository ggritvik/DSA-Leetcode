# nums = [100,4,200,1,3,2]
# # nums = []
# counts = []
# count = 0


# nums = sorted(nums)
# nums2 = []

# for i in nums:
#     if i not in nums2:
#         nums2.append(i)

# print(nums2)

# if len(nums) == 0:
#     print("12")
#     exit()

# l = 0
# r = 1

# while r < len(nums2):
#     if nums[l]+1 == nums[r]:
#         count += 1
#         l += 1
#         r += 1
#     else:
#         counts.append(count)
#         count = 0
#         l = r
#         r += 1

# counts.append(count)  
# print(max(counts) + 1) 


nums = [100,4,200,1,3,2]

num_set = set(nums)
longest_streak = 0

for num in num_set:
    if num-1 not in num_set:

        current_num = num
        current_streak = 1

        while current_num +1 in num_set:
            current_num += 1
            current_streak += 1
        longest_streak = max(longest_streak, current_streak)
print(longest_streak)