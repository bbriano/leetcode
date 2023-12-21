class Solution:
	def myAtoi(self, s: str) -> int:
		i = 0
		while i < len(s) and s[i] == " ":
			i += 1
		if i < len(s) and s[i] in "-+":
			i += 1
		if i >= len(s) or s[i] not in "0123456789":
			return 0
		i += 1
		while i < len(s) and s[i] in "0123456789":
			i += 1
		out = int(s[:i])
		if out < -2**31:
			out = -2**31
		if out > 2**31-1:
			out = 2**31-1
		return out

def test():
	test_cases = [
		(["42"], 42),
		(["-42"], -42),
		(["4193 with words"], 4193),
		(["words and 987"], 0),
		([""], 0),
		(["-91283472332"], -2**31),
		(["91283472332"], 2**31-1),
		(["+"], 0),
	]
	for inp,out in test_cases:
		got = Solution().myAtoi(*inp)
		assert got == out, "myAtoi(%s) = %s, want %s" % (inp, got, out)

if __name__ == "__main__":
	test()
