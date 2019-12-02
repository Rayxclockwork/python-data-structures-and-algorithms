arr = [1, 2, 3]
newArr = []

def reverseArray():
  i = len(arr) -1
  while i >= 0:
    newArr.append(arr[i])
    i -= 1

reverseArray()
print(newArr)
