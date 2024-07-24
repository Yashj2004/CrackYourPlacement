def ceiling_element(nums, x):
  start=0
  end=len(nums)
  if nums[start]>x:
    return nums[start]
  for i in range(start,end):
    if nums[i]==x:
      return x
    if nums[i]<x and nums[i+1]>=x:
      return nums[i+1]
  return -1
arr = [1, 2, 8, 10, 10, 12, 19]
print(ceiling_element(arr, 5))
