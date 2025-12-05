# nums = [1,1,2,2,3,4,4]
# lenght = len(nums)

# hash_set = set()

# for i in nums:
#     if i not in hash_set:
#         hash_set.add(i)
#     else:
#         continue

# result= list(hash_set)
# length_final = len(result)

# differnce = lenght - length_final

# #add a _ to the end of the list for each duplicate removed


# for i in range(differnce):
#     result.append("_")

# print (result)


def remove_duplicates(nums):
    # Initialize a pointer for the position of unique elements
    unique_index = 0

    # Iterate through the array
    for i in range(1, len(nums)):
        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i]

    # Calculate the number of duplicates
    duplicates_count = len(nums) - (unique_index + 1)

    # Replace duplicates with underscores
    for i in range(duplicates_count):
        nums[unique_index + 1 + i] = "_"

    return nums

# Example usage
nums = [1, 1, 2, 2, 3, 4, 4]
result = remove_duplicates(nums)
print(result)