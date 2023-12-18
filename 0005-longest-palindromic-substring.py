class Solution:
	def longestPalindrome(self, s: str) -> str:
		def expand(left, right):
			while left >= 0 and right < len(s) and s[left] == s[right]:
				left -= 1
				right += 1
			return s[left+1:right]
		max = ""
		for i in range(len(s)):
			odd = expand(i, i)
			if len(odd) > len(max):
				max = odd
			even = expand(i, i+1)
			if len(even) > len(max):
				max = even
		return max

def test():
	test_cases = [
		(["babad"], "bab"),
		(["cbbd"], "bb"),
		([""], ""),
		(["x"], "x"),
	]
	for inp,out in test_cases:
		got = Solution().longestPalindrome(*inp)
		assert got == out, "longestPalindrome(%s) = %s, want %s" % (inp, got, out)

if __name__ == "__main__":
	test()
