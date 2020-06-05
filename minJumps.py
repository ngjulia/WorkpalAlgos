import numpy

arr = [1, 1, 5, 8, 9, 2, 6, 7, 6, 8, 9]

# greedy approach
def minJumps(arr):
  print(arr)
  j = 0
  i = 0
  while (i < len(arr)-1):
    jump = arr[i]-numpy.argmax(arr[i+1:i+1+arr[i]][::-1])
    j += 1
    i = i + jump
  return j

print(minJumps(arr))
