nums = [100,4,200,1,3,2]

#! make a set to remove the duplicates and allow O(1) lookups
num_set = set(nums)
longest_streak = 0

for num in nums:
#! Basically the starting of sequences always never have a left neighbor, so by checking n-1 we find start of sequences
    if num-1 not in num_set: 
        current_num = num #! Start from that number
        current_streak = 1

        while current_num+1 in num_set: #! runs as long as a sequence number is found
            current_num += 1
            current_streak += 1
#! we basically compare the sequence length for each found sequence and store the max length found so far
        longest_streak = max(longest_streak, current_streak) 
#! Finally print the longest sequence found
print(longest_streak)


#! whole equation runs in O(n) time complexity because each number is processed at most twice