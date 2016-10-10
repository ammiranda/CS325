def max_min(arr):
  if len(arr) == 1:
    return (arr[0], arr[0])
  elif len(arr) == 2:
    if arr[0] < arr[1]:
      return (arr[0], arr[1])
    else:
      return (arr[1], arr[0])
  else:
    mid_point = int(len(arr) / 2)
    (min_left, max_left) = max_min(arr[0:mid_point])
    (min_right, max_right) = max_min(arr[(mid_point + 1):])

    if max_left < max_right:
      maximum = max_right
    else:
      maximum = max_left

    if min_left < min_right:
      minimum = min_left
    else:
      minimum = min_right

    return (minimum, maximum)

print(max_min([1, 40, 30, 100, -6]))
