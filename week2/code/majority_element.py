import math

def get_frequency(arr, el):
  count = 0
  for i in arr:
    if i == el:
      count += 1

  return count

def find_majority_el(arr):
  if len(arr) == 1:
    return arr[0]
  k = math.floor(len(arr) / 2)
  left_majority = find_majority_el(arr[0:k])
  right_majority = find_majority_el(arr[k:])

  print("%d, %d" % (left_majority, right_majority))

  if left_majority == right_majority:
    return left_majority

  lcount = get_frequency(arr, left_majority)
  rcount = get_frequency(arr, right_majority)

  if lcount > k + 1:
    return left_majority
  elif rcount > k + 1:
    return right_majority
    


l = [0, 1, 1, 1, 4, 4, 4, 4, 4, 4]
print(find_majority_el(l))
