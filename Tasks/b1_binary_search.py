from typing import Any, Sequence, Optional


def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array
	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	n = len(arr)
	l = 0
	r = n - 1

	while l <= r:
		m = int((l + r) / 2)
		if arr[m] < elem:
			l = m + 1
		elif arr[m] > elem:
			r = m - 1
		else:
			return m
	return None
