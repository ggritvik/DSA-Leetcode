nums = [2,2,2,2,1,1,3,3,3]
k = 2

count = {}
hash_set = set()

for num in nums:
    if num in hash_set:
        count[num] += 1
    else:
        count[num] = 1
        hash_set.add(num)

    sorted_count = sorted(count.keys(), #basically signifies what will be represented after sorting --> as we need only keys so count.keys
                          key=lambda x: count[x],  #signifies the thing to be sorted --> count[x] = values
                          reverse=True)[:k]  #order of sorting ascending or descending

print(sorted_count)
