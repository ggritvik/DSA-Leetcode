nums = [2,7,11,15]
target = 17

hash_set = set()
for i,n in enumerate(nums):
    print(i,n)
    compliment = target - n
    if compliment in hash_set:
        print([nums.index(compliment),i])
    else:
        hash_set.add(n)


# complement = target - nums[0]
# print (nums.index(complement))

# WILL WORK FOR TWOSOME2 AS WELL BUT IN THAT WE HAVE TO USE THE CONCEPT OF TWO POINTERS
