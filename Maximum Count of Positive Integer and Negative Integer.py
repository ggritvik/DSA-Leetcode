nums = [-2,-1,-1,0,0,1,2,3]

# Brute Force Solution
def maxCount(nums):
    positve_count = 0
    negative_count = 0

    for i in nums:
        if i<0:
            negative_count += 1
        
        elif i == 0:
            continue
        
        else:
            positve_count += 1

    return max(positve_count, negative_count)


print(maxCount(nums))
