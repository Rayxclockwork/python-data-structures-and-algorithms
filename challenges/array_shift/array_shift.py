def insert_shift_array(lst, val)
  result = []
  key_index = (len(lst) + 1) // 2
  for i in range(0, key_index):
    result.append(lst[i])
    result.append(val)
  for i in range(key_index, len(lst)):
    result.append(lst[i])

  return result