class Solution:
	def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
		n = len(nums)
		good = []
		seen = set()
		for i in range(n-3):
			if nums[i] in seen:
				continue
			seen.add(nums[i])
			for sol in self.threeSum(nums[i+1:], target-nums[i]):
				tmp = [nums[i]] + sol
				tmp.sort()
				good.append(tmp)
		if len(good) == 0:
			return []
		good.sort()
		out = [good[0]]
		for i in range(1, len(good)):
			if good[i] != good[i-1]:
				out.append(good[i])
		return out

	def threeSum(self, nums: list[int], target: int) -> list[list[int]]:
		out = []
		nums.sort()
		i = 0
		while i < len(nums)-2:
			j = i+1
			k = len(nums)-1
			while j < k:
				s = nums[i] + nums[j] + nums[k]
				if s < target:
					j += 1
					while j < len(nums) and nums[j] == nums[j-1]:
						j += 1
				elif s > target:
					k -= 1
					while k > j and nums[k] == nums[k+1]:
						k -= 1
				else:
					out.append([nums[i], nums[j], nums[k]])
					j += 1
					while j < len(nums) and nums[j] == nums[j-1]:
						j += 1
					k -= 1
					while k > j and nums[k] == nums[k+1]:
						k -= 1
			i += 1
			while i < len(nums) and nums[i] == nums[i-1]:
				i += 1
		return out

class SolutionBruteforce:
	def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
		good = []
		n = len(nums)
		for i in range(n-3):
			for j in range(i+1, n-2):
				for k in range(j+1, n-1):
					for l in range(k+1, n):
						if nums[i] + nums[j] + nums[k] + nums[l] == target:
							a = [nums[i], nums[j], nums[k], nums[l]]
							a.sort()
							good.append(a)
		if len(good) == 0:
			return []
		good.sort()
		out = [good[0]]
		for i in range(1, len(good)):
			if good[i] != good[i-1]:
				out.append(good[i])
		return out

def test(sol):
	test_cases = [
		([[1, 0, -1, 0, -2, 2], 0], [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
		([[2, 2, 2, 2, 2], 8], [[2, 2, 2, 2]]),
	]
	for inp,out in test_cases:
		got = sol().fourSum(*inp)
		assert got == out, "fourSum(%s) = %s, want %s" % (inp, got, out)

if __name__ == "__main__":
	test(Solution)
	test(SolutionBruteforce)
	from timeit import timeit
	print(timeit('test(Solution)', globals=globals()))
	print(timeit('test(SolutionBruteforce)', globals=globals()))
