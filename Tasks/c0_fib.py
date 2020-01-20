def fib_recursive(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using recursive algorithm

	:param n: number of item
	:return: Fibonacci number
	"""
	if n < 1:
		myError = ValueError('n should be >= 1')
		raise myError

	if n >= 3:
		return fib_recursive(n-1)+fib_recursive(n-2)
	else:
		return 1


def fib_iterative(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using iterative algorithm

	:param n: number of item
	:return: Fibonacci number

	"""
	if n < 1:
		myError = ValueError('n should be >= 1')
		raise myError

	p0 = 1
	p1 = 1
	i = 3

	while i <= n:
		temp = p0 + p1
		p0 = p1
		p1 = temp
		i += 1
	return p1
