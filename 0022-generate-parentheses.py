class Solution:
	cache = {1: ["()"]}
	def generateParenthesis(self, n: int) -> list[str]:
		if n in self.cache:
			return self.cache[n]
		out = []
		for sub in self.generateParenthesis(n-1):
			out.append("(" + sub + ")")
		for left in range(1, n):
			right = n - left
			for l in self.generateParenthesis(left):
				for r in self.generateParenthesis(right):
					sol = l + r
					if sol not in out:
						out.append(sol)
		self.cache[n] = out
		return out

	def generateParenthesisSorted(self, n: int) -> list[str]:
		return sorted(self.generateParenthesis(n))

def test(sol):
	test_cases = [
		([1], ["()"]),
		([2], ["(())", "()()"]),
		([3], ["((()))", "(()())", "(())()", "()(())", "()()()"]),
	]
	for inp,out in test_cases:
		got = sol().generateParenthesisSorted(*inp)
		assert got == out, "generateParenthesisSorted(%s) = %s, want %s" % (inp, got, out)

if __name__ == "__main__":
	test(Solution)
