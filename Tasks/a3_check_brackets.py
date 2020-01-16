def check_brackets(brackets_row: str) -> bool:
	"""
	Check whether input string is a valid bracket sequence
	Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
	:param brackets_row: input string to be checked
	:return: True if valid, False otherwise
	"""
	n = len(brackets_row)
	counter = 0
	for i in range(n):
		if brackets_row[i] == "(":
			counter += 1
		elif brackets_row[i] == ")":
			counter -= 1
			if counter < 0:
				return False
	if counter == 0:
		return True
	else:
		return False
