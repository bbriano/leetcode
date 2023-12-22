class Solution:
	def isPalindrome(self, x: int) -> bool:
		if x < 0:
			return False
		s = str(x)
		for i in range(len(s)//2):
			if s[i] != s[-1-i]:
				return False
		return True

def test():
	test_cases = [
		([121], True),
		([-121], False),
		([10], False),
		([0], True),
	]
	for inp,out in test_cases:
		got = Solution().isPalindrome(*inp)
		assert got == out, "isPalindrome(%s) = %s, want %s" % (inp, got, out)

if __name__ == "__main__":
	test()
