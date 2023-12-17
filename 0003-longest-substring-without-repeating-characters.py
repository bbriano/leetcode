class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		maxn = 0
		n = 0
		idx = [len(s) for _ in range(128)]
		for i in range(len(s)-1, -1, -1):
			n = min(idx[ord(s[i])]-i, n+1)
			if n > maxn:
				maxn = n
			idx[ord(s[i])] = i
		return maxn

class SolutionSlow:
	def lengthOfLongestSubstring(self, s: str) -> int:
		maxlen = 0
		for i in range(len(s)):
			for j in range(i, len(s)):
				substr = s[i:j+1]
				if not self.repeat(substr) and len(substr) > maxlen:
					maxlen = len(substr)
		return maxlen

	def repeat(self, s: str) -> bool:
		count = dict()
		for c in s:
			if c in count:
				count[c] += 1
			else:
				count[c] = 1
		return max(count.values()) > 1

def test():
	test_cases = [
		(["abcabcbb"], 3),
		(["bbbbb"], 1),
		(["pwwkew"], 3),
	]
	for inp,out in test_cases:
		got = Solution().lengthOfLongestSubstring(*inp)
		assert got == out, "lengthOfLongestSubstring(%s) = %s, want %s" % (inp, got, out)

if __name__ == "__main__":
	test()
