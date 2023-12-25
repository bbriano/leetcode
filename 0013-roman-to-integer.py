class Solution:
	def romanToInt(self, s: str) -> int:
		out = 0
		while len(s) > 0:
			if s[0] == "M":
				out += 1000
				s = s[1:]
			elif s[0:2] == "CM":
				out += 900
				s = s[2:]
			elif s[0] == "D":
				out += 500
				s = s[1:]
			elif s[0:2] == "CD":
				out += 400
				s = s[2:]
			elif s[0] == "C":
				out += 100
				s = s[1:]
			elif s[0:2] == "XC":
				out += 90
				s = s[2:]
			elif s[0] == "L":
				out += 50
				s = s[1:]
			elif s[0:2] == "XL":
				out += 40
				s = s[2:]
			elif s[0] == "X":
				out += 10
				s = s[1:]
			elif s[0:2] == "IX":
				out += 9
				s = s[2:]
			elif s[0] == "V":
				out += 5
				s = s[1:]
			elif s[0:2] == "IV":
				out += 4
				s = s[2:]
			elif s[0] == "I":
				out += 1
				s = s[1:]
		return out

def test(sol):
	test_cases = [
		(["III"], 3),
		(["LVIII"], 58),
		(["MCMXCIV"], 1994),
	]
	for inp,out in test_cases:
		got = sol().romanToInt(*inp)
		assert got == out, "romanToInt(%s) = %s, want %s" % (inp, got, out)

if __name__ == "__main__":
	test(Solution)
