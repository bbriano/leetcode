
class Solution:
	def isValid(self, s: str) -> bool:
		stack = []
		for c in s:
			if c in "([{":
				stack.append(c)
			else:
				if len(stack) == 0:
					return False
				last = stack.pop()
				if c == ")" and last != "(":
					return False
				elif c == "]" and last != "[":
					return False
				elif c == "}" and last != "{":
					return False
		return len(stack) == 0

def test(sol):
	test_cases = [
		(["()"], True),
		(["()[]{}"], True),
		(["(]"], False),
		([""], True),
		(["(()"], False),
	]
	for inp,out in test_cases:
		got = sol().isValid(*inp)
		assert got == out, "isValid(%s) = %s, want %s" % (inp, got, out)

if __name__ == "__main__":
	test(Solution)
