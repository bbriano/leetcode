class Solution:
	def convert(self, s: str, numRows: int) -> str:
		if numRows == 1:
			return s
		out = []
		chunk = 2*(numRows-1)
		s = s + "$" * (chunk - len(s)%chunk)
		nchunk = len(s) // chunk
		for j in range(nchunk):
			out.append(s[j*chunk])
		for i in range(1, chunk//2):
			for j in range(nchunk):
				out.append(s[j*chunk + i])
				out.append(s[(j+1)*chunk - i])
		for j in range(nchunk):
			out.append(s[j*chunk + chunk//2])
		for i in range(len(out)):
			if out[i] == "$":
				out[i] = ""
		return "".join(out)

def test():
	test_cases = [
		(["PAYPALISHIRING", 5], "PHASIYIRPLIGAN"),
		(["PAYPALISHIRING", 3], "PAHNAPLSIIGYIR"),
		(["PAYPALISHIRING", 4], "PINALSIGYAHRPI"),
		(["", 1], ""),
		(["A", 1], "A"),
		(["AB", 1], "AB"),
	]
	for inp,out in test_cases:
		got = Solution().convert(*inp)
		assert got == out, "convert(%s) = %s, want %s" % (inp, got, out)

if __name__ == "__main__":
	test()
