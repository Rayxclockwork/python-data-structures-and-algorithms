arr = [1, 2, 3]
newArr = []

i = len(arr) - 1
def reverseArray():
  while i >= 0:
    newArr.append(arr[i])
    i -= 1
    print(newArr)

reverseArray()