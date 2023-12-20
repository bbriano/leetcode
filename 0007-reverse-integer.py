class Solution:
	def reverse(self, x: int) -> int:
		neg = "-" if x < 0 else ""
		out = int(neg + str(abs(x))[::-1])
		if out < -2**31 or out > 2**31-1:
			return 0
		return out

def test():
	test_cases = [
		([123], 321),
		([-123], -321),
		([120], 21),
		([1534236469], 0),
	]
	for inp,out in test_cases:
		got = Solution().reverse(*inp)
		assert got == out, "reverse(%s) = %s, want %s" % (inp, got, out)

if __name__ == "__main__":
	test()
