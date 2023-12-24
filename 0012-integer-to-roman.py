class Solution:
	def intToRoman(self, num: int) -> str:
		out = []
		while num > 0:
			if num >= 1000:
				out.append("M")
				num -= 1000
			elif num >= 900:
				out.append("CM")
				num -= 900
			elif num >= 500:
				out.append("D")
				num -= 500
			elif num >= 400:
				out.append("CD")
				num -= 400
			elif num >= 100:
				out.append("C")
				num -= 100
			elif num >= 90:
				out.append("XC")
				num -= 90
			elif num >= 50:
				out.append("L")
				num -= 50
			elif num >= 40:
				out.append("XL")
				num -= 40
			elif num >= 10:
				out.append("X")
				num -= 10
			elif num >= 9:
				out.append("IX")
				num -= 9
			elif num >= 5:
				out.append("V")
				num -= 5
			elif num >= 4:
				out.append("IV")
				num -= 4
			else:
				out.append("I")
				num -= 1
		return "".join(out)

def test(sol):
	test_cases = [
		([3], "III"),
		([58], "LVIII"),
		([1994], "MCMXCIV"),
	]
	for inp,out in test_cases:
		got = sol().intToRoman(*inp)
		assert got == out, "intToRoman(%s) = %s, want %s" % (inp, got, out)

if __name__ == "__main__":
	test(Solution)
