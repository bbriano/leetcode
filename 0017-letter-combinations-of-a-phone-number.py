class Solution:
	phone = {
		"2": ["a", "b", "c"],
		"3": ["d", "e", "f"],
		"4": ["g", "h", "i"],
		"5": ["j", "k", "l"],
		"6": ["m", "n", "o"],
		"7": ["p", "q", "r", "s"],
		"8": ["t", "u", "v"],
		"9": ["w", "x", "y", "z"],
	}
	def letterCombinations(self, digits: str) -> list[str]:
		if len(digits) == 0:
			return []
		out = self.phone[digits[-1]]
		for d in reversed(digits[:-1]):
			new = []
			for head in self.phone[d]:
				for tail in out:
					new.append(head + tail)
			out = new
		return out

class SolutionRecursive:
	phone = {
		"2": ["a", "b", "c"],
		"3": ["d", "e", "f"],
		"4": ["g", "h", "i"],
		"5": ["j", "k", "l"],
		"6": ["m", "n", "o"],
		"7": ["p", "q", "r", "s"],
		"8": ["t", "u", "v"],
		"9": ["w", "x", "y", "z"],
	}
	def letterCombinations(self, digits: str) -> list[str]:
		if len(digits) == 0:
			return []
		if len(digits) == 1:
			return self.phone[digits]
		out = []
		for head in self.phone[digits[0]]:
			for tail in self.letterCombinations(digits[1:]):
				out.append(head + tail)
		return out

def test(sol):
	test_cases = [
		(["23"], ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
		([""], []),
		(["2"], ["a", "b", "c"]),
		(["999"], ["www", "wwx", "wwy", "wwz", "wxw", "wxx", "wxy", "wxz", "wyw", "wyx", "wyy", "wyz", "wzw", "wzx", "wzy", "wzz", "xww", "xwx", "xwy", "xwz", "xxw", "xxx", "xxy", "xxz", "xyw", "xyx", "xyy", "xyz", "xzw", "xzx", "xzy", "xzz", "yww", "ywx", "ywy", "ywz", "yxw", "yxx", "yxy", "yxz", "yyw", "yyx", "yyy", "yyz", "yzw", "yzx", "yzy", "yzz", "zww", "zwx", "zwy", "zwz", "zxw", "zxx", "zxy", "zxz", "zyw", "zyx", "zyy", "zyz", "zzw", "zzx", "zzy", "zzz"]),
	]
	for inp,out in test_cases:
		got = sol().letterCombinations(*inp)
		assert got == out, "letterCombinations(%s) = %s, want %s" % (inp, got, out)

if __name__ == "__main__":
	test(Solution)
	test(SolutionRecursive)
	from timeit import timeit
	print(timeit('test(Solution)', globals=globals()))
	print(timeit('test(SolutionRecursive)', globals=globals()))
