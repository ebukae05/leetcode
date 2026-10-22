#arrays
arr = [1,2,3]
print(arr)

#adding to the array
arr.append(4)
arr.append(5)
print(arr)

#removing from array
arr.pop()
print(arr)

#at index[1] insert 7
arr.insert(1, 7)
print(arr)

#variables

arr[0] = 0
print(arr)

n = 5
arr = [1] * n
print(arr)
print(len(arr))

#array slicing
arr = [1,2,3,4]
print(arr[1:3])
print(arr[0:4])

#unpacking
a,b,c = [1,2,3]
print(a)
print(b)
print(c)

#loop through arrays
nums = [1,2,3]

#using index
for i in range(len(nums)):
    print(nums[i])

#Without index
for n in nums:
    print(n)

# with index and value
for i, n in enumerate(nums):
   print(i, n)

# loop through multiple arrays simultaneously
# [unpacking]

nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1,n2 in zip(nums1, nums2):
   print(n1, n2)

# reverse
nums = [1,2,3]
nums.reverse()
print(nums)

