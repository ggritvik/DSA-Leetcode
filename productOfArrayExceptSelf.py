nums = [-1,1,0,-3,3]
output = [1]* len(nums)

for i in range(1, len(nums)):
    output[i] = output[i-1] * nums[i-1]

right = nums[-1]
for i in range(len(nums)-2, -1, -1):
    output[i] = output[i] * right
    right *= nums[i]

print(output)



# https://www.youtube.com/watch?v=5bS636lE_R0&t=292s <---- Solution