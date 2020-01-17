def partition(arr, left_pointer, right_pointer):

	pivot_position = right_pointer

	pivot_value = arr[pivot_position]

	right_pointer -= 1

	while True:
		while arr[left_pointer] < pivot_value:
			left_pointer += 1
		
		while arr[right_pointer] > pivot_value:
			right_pointer -= 1

		if left_pointer >= right_pointer:
			break
		else:
			swap(arr, left_pointer, right_pointer)

	swap(arr, left_pointer, pivot_position)
	return left_pointer


def swap(arr, left_index, right_index):
	arr[left_index], arr[right_index] = arr[right_index], arr[left_index]


if __name__ == '__main__':
	def quick_sort(arr, left_index, right_index):
		
		if right_index - left_index <= 0:
			return
		
		pivot_position = partition(arr, left_index, right_index)

		quick_sort(arr, left_index, pivot_position-1)

		quick_sort(arr, pivot_position+1, right_index)