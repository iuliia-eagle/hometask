"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any

queue = []

def enqueue(elem: Any, priority: int = 0) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	global queue
	queue.append((priority, elem))
	queue.sort(key=lambda x:x[0])
	return None


def dequeue() -> Any:
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	global queue
	if queue:
		elem = queue.pop(0)
		return elem[1]
	else:
		return None


def peek(ind: int = 0, priority: int = 0) -> Any:
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	global queue
	elem = queue[ind]
	return elem[1]


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	global queue
	while queue:
		queue.pop()
	#	dequeue()
	#queue[:] = []
	return None
