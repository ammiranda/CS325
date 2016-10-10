def max_min(arr):
  if len(arr) == 1:
    return (arr[0], arr[0])
  elif len(arr) == 2:
    if arr[0] > arr[1]:
      return (arr[0], arr[1])
    else:
      return (arr[1], arr[0])
  else:
    minimum = float("inf")
    maximum = float("-inf")

    for i in arr:
      if i > maximum:
        maximum = i
      
      if i < minimum:
        minimum = i

    return (minimum, maximum)


print(max_min([1, 30, 100, -3]))
