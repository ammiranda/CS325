# hotels is an array containing hotel objects with the following form:
# { 'distance': int, 'id': str }

def road_trip(hotels, daily_dist):
  hotels_slept_in = []
  dist_done = 0
  i = 0
  cur_hotel = hotels[i]

  while cur_hotel['id'] != hotels[len(hotels) - 1]['id']:
    dist_diff = dist_done + daily_dist
    while dist_diff >= 0 and i + 1 < len(hotels):
      cur_hotel = hotels[i]
      dist_done += cur_hotel['distance'] - dist_done
      dist_diff -= dist_done
      i += 1
    hotels_slept_in.append(cur_hotel)

  return hotels_slept_in


print(road_trip([{'distance': 5, 'id': 'a'}, {'distance': 15, 'id':'b'}, {'distance': 25, 'id': 'c'}, {'distance': 31, 'id': 'f'}], 5))

  
