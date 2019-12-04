def insert_shift_array(lst, val):
  result = []
  key_index = (len(lst) + 1) // 2
  for i in range(0, key_index):
    result.append(lst[i]) 
    result.append(val)
  for i in range(key_index, len(lst)):
    result.append(lst[i])

  # return result
# print(insert_shift_array([1, 2, 4, 5], 3))


def insert_array_shift(lst, val):
  if len(lst) % 2 == 0:
    mid = len(lst) //2
    new_lst =lst[:mid] + [val] + lst[mid:]
    return new_lst

  elif len(lst) % 2 == 1:
    mid = len(lst) //2 + 1
    new_lst =lst[:mid]+[val]+lst[mid:]
    return new_lst
print(insert_shift_array([1, 2, 4, 5], 3))