class Solution:
	def maxArea(self, height: list[int]) -> int:
		left = [0]
		for i in range(len(height)):
			if height[i] > height[left[-1]]:
				left.append(i)
		right = [len(height)-1]
		for i in range(len(height)-1, -1, -1):
			if height[i] > height[right[-1]]:
				right.append(i)
		maxarea = 0
		i = 0
		for l in left:
			while i < len(right):
				r = right[i]
				area = (r-l) * min(height[l], height[r])
				if area > maxarea:
					maxarea = area
				if height[r] >= height[l]:
					break
				i += 1
		return maxarea

class SolutionSlow:
	def maxArea(self, height: list[int]) -> int:
		left = [0]
		for i in range(len(height)):
			if height[i] > height[left[-1]]:
				left.append(i)
		right = [len(height)-1]
		for i in range(len(height)-1, -1, -1):
			if height[i] > height[right[-1]]:
				right.append(i)
		maxarea = 0
		for l in left:
			for r in right:
				area = (r-l) * min(height[l], height[r])
				if area > maxarea:
					maxarea = area
		return maxarea

class SolutionSlowSlow:
	def maxArea(self, height: list[int]) -> int:
		maxarea = 0
		for i in range(len(height)-1):
			for j in range(i+1, len(height)):
				area = (j-i) * min(height[i], height[j])
				if area > maxarea:
					maxarea = area
		return maxarea

def test(sol):
	test_cases = [
		([[1,8,6,2,5,4,8,3,7]], 49),
		([[1,1]], 1),
		([[25, 55, 19, 38, 86, 30, 49, 44, 14, 62, 99, 41, 100, 63, 39, 77, 47, 37, 14, 92, 49, 9, 5, 14, 7, 3, 45, 21, 31, 4, 9, 23, 39, 44, 7, 84, 96, 5, 1, 55, 7, 49, 3, 94, 17, 90, 9, 83, 59, 63, 97, 94, 32, 4, 20, 69, 28, 18, 38, 43, 75, 72, 59, 31, 82, 10, 49, 15, 61, 38, 51, 9, 40, 83, 10, 95, 62, 2, 30, 35, 92, 41, 12, 33, 3, 74, 32, 51, 56, 43, 42, 76, 95, 85, 42, 2, 50, 92, 88, 48]], 8084),
		([[428, 865, 689, 967, 77, 957, 78, 841, 600, 905, 87, 412, 364, 364, 751, 44, 312, 176, 360, 751, 379, 881, 258, 547, 754, 373, 391, 962, 741, 906, 238, 648, 459, 512, 307, 408, 70, 827, 335, 540, 873, 311, 175, 469, 712, 177, 133, 291, 488, 510, 815, 862, 805, 923, 609, 820, 705, 259, 89, 537, 321, 379, 264, 854, 488, 257, 95, 535, 361, 575, 342, 718, 583, 775, 701, 7, 837, 636, 712, 186, 471, 126, 752, 780, 483, 367, 613, 316, 303, 278, 75, 152, 317, 193, 859, 514, 124, 807, 157, 225]], 79887),
	]
	for inp,out in test_cases:
		got = sol().maxArea(*inp)
		assert got == out, "maxArea(%s) = %s, want %s" % (inp, got, out)

if __name__ == "__main__":
	test(Solution)
	test(SolutionSlow)
	test(SolutionSlowSlow)
