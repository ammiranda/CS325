def majority_element(arr):
  counter = 0
  possible_element = None

  for i in arr:
    if counter == 0:
      possible_element = i
      counter = 1
    elif i == possible_element:
      counter += 1
    else:
      counter -= 1

  return possible_element

l = [1, 4, 4, 4]
print(majority_element(l))
