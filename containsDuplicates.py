nums = [1,2,3,4,1]
# def ContainsDuplicate(nums):
#     hash_set = set()
#     for num in nums:
#         if num in hash_set:
#             return True 
#         else:
#             hash_set.add(num)
#     return False            


# isDuplicate = ContainsDuplicate(nums)
# print(isDuplicate)


hash_set = set(nums)
if(len(hash_set) == len(nums)):
    print(False)
else:
    print(True)