#!/usr/bin/python3

def make_change(coin_val_list, change, known_results):
  min_coins = change
  if change in coin_val_list:
    known_results[change] = 1
    return 1
  elif known_results[change] > 0:
    return known_results[change]
  else:
    for i in [c for c in coin_val_list if c <= change]:
      num_coins = 1 + make_change(coin_val_list, change - i, known_results)
      if num_coins < min_coins:
        min_coins = num_coins
        known_results[change] = min_coins
  return min_coins

print(make_change([1, 3, 4], 11, [0]*64))
print(make_change([1, 10, 25, 50], 40, [0]*64))
    
