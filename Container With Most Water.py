height = [1,8,6,2,5,4,8,3,7]
# new = []

# for i in range(len(height)):
#     for j in range(i+1, len(height)):
#         area = min(height[i], height[j]) * (j-i)      ## BRUTE FORCE APPROACH
#         new.append(area)
        
# print(max(new))

l,r=0,len(height)-1
res = 0

while l<r:
    area = min(height[l], height[r]) * (r-l)
    res = max(res, area)                                ## TWO POINTER APPROACH
    if height[l] < height[r]:
        l+=1
    elif height[l] == height[r]:
        l+=1
    else:
        r-=1

print(res)