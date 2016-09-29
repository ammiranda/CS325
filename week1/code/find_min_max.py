def find_min_max(arr):
  ans = {}
  for x in arr:
    if 'min' in ans:
      if x < ans['min']:
        ans['min'] = x
    else:
      ans['min'] = x
    
    if 'max' in ans: 
      if x > ans['max']:
        ans['max'] = x
    else:
      ans['max'] = x
    
  return ans

example = find_min_max([9, 3, 5, 10, 1, 7, 12])

print("Max: %d Min: %d" % (example['max'], example['min']))
