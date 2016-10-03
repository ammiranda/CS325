def find_min_max(arr):
    start_index = None
    comparisons = 0

    if len(arr) % 2 == 0:
      if arr[0] > arr[1]:
        max_val = arr[0]
        min_val = arr[1]
      else:
        max_val = arr[1]
        min_val = arr[0]              
      start_index = 2
      comparisons += 1
    else:
      max_val = arr[0]
      min_val = arr[0]
      start_index = 1

    for i in range(start_index, len(arr) - 1):

        if arr[i] < arr[i + 1]:
            if arr[i] < min_val:
                min_val = arr[i]
            if arr[i + 1] > max_val:
                max_val = arr[i + 1]
            comparisons += 2
        else:
            if arr[i + 1] < min_val:
                min_val = arr[i + 1]
            if arr[i] > max_val:
                max_val = arr[i]
            comparisons += 2
                
    print(comparisons, len(arr))
    return {'max': max_val, 'min': min_val}

example = find_min_max([40, 9, 3, 5, 10, 1, 7, 12])

print("Max: %d Min: %d" % (example['max'], example['min']))
