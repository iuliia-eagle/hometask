"""
Taylor series
"""
from typing import Union


def ex(x: Union[int, float]) -> float:
	"""
	Calculate value of e^x with Taylor series

	:param x: x value
	:return: e^x value
	"""
	result = 0.0
	factorial = 1

	for n in range(10):
		result += (x ** n) / factorial
		factorial *= n + 1
	return result


def sinx(x: Union[int, float]) -> float:
	"""
	Calculate sin(x) with Taylor series

	:param x: x value
	:return: sin(x) value
	"""
	result = 0.0
	factorial = 1

	for n in range(5):
		result += (-1) ** n * (x ** (2*n + 1)) / factorial
		factorial *= (2 * n + 2) * (2 * n + 3)
	return result

