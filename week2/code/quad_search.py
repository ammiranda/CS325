def quad_search(arr, el):
  start = 0
  first_quarter = int(len(arr) / 4) - 1
  mid_point = int(len(arr) / 2) - 1
  third_quarter = int(len(arr) * (3 / 4)) - 1
  end = len(arr) - 1

  list_of_quads = [start, first_quarter, mid_point, third_quarter, end]

  try:
    index = [arr[i] for i in list_of_quads].index(el)
    return list_of_quads[index]
  except:
    pass

  if (arr[start] < el < arr[first_quarter]):
    return quad_search(arr[start:first_quarter], el)
  elif (arr[first_quarter] < el < arr[mid_point]):
    return quad_search(arr[first_quarter:mid_point], el)
  elif (arr[mid_point] < el < arr[third_quarter]):
    return quad_search(arr[mid_point:third_quarter], el)
  elif (arr[third_quarter] < el < arr[end]):
    return quad_search(arr[third_quarter:end], el)
  else:
    return -1

print(quad_search([1,2], 3))
print(quad_search([10, 12, 24, 56], 10))
print(quad_search([2, 4, 6, 8, 10], 6))
