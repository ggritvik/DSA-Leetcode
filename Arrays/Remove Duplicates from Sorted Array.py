nums = [0,0,1,1,1,2,2,3,3,4]

#! its a two pointer approach for the first pointer 'l' to just keep track of position to enter the uniques element

#! r pointer keep searching the array and whenever it finds a unique element it places it at l and increments l

#! Leetcode wanted the number of unique elements so we print l at the end and not the array

l = 1

for r in range(1, len(nums)):
    if nums[r] != nums[r-1]:

        nums[l] = nums[r]
        l = l+1

print(l)
