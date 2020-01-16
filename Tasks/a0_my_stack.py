"""
My little Stack
"""
from typing import Any

stack = []

def push(elem: Any) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	global stack
	stack.append(elem)
	return None


def pop() -> Any:
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	global stack
	if stack:
		elem = stack.pop(-1)
		return elem
	else:
		return None


def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	global stack
	elem = stack[-ind-1]
	return elem


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	while stack:
		stack.pop()
	return None
