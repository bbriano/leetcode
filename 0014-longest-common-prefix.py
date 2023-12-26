class Solution:
	def longestCommonPrefix(self, strs: list[str]) -> str:
		strs = sorted(strs)
		a, b = strs[0], strs[-1]
		i, minlen = 0, min(len(a), len(b))
		while i < minlen:
			if a[i] != b[i]:
				return a[:i]
			i += 1
		return a[:i]

class SolutionSlow:
	def longestCommonPrefix(self, strs: list[str]) -> str:
		minlen = 999
		for s in strs:
			if len(s) < minlen:
				minlen = len(s)
		i = 0
		while i < minlen:
			for j in range(len(strs)-1):
				if strs[j][i] != strs[j+1][i]:
					return strs[0][:i]
			i += 1
		return strs[0][:i]

def test(sol):
	test_cases = [
		([["flower", "flow", "flight"]], "fl"),
		([["dog", "racecar", "car"]], ""),
		([["flower", "flow"]], "flow"),
		([["flowerflowerflowerflowerflowerflowerflowerflower", "flow", "flow", "flow", "flow"]], "flow"),
	]
	for inp,out in test_cases:
		got = sol().longestCommonPrefix(*inp)
		assert got == out, "longestCommonPrefix(%s) = %s, want %s" % (inp, got, out)

if __name__ == "__main__":
	test(Solution)
	test(SolutionSlow)
