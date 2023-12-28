class SolutionFast:
	def threeSum(self, nums: list[int]) -> list[list[int]]:
		out = []
		nums.sort()
		i = 0
		while i < len(nums)-2:
			j = i+1
			k = len(nums)-1
			while j < k:
				s = nums[i] + nums[j] + nums[k]
				if s < 0:
					j += 1
					while j < len(nums) and nums[j] == nums[j-1]:
						j += 1
				elif s > 0:
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

	def testfunc(self, nums: list[int]) -> list[list[int]]:
		return sorted(map(sorted, self.threeSum(nums)))

class Solution:
	def threeSum(self, nums: list[int]) -> list[list[int]]:
		nums = sorted(nums)
		maybe = []
		seen = {nums[0]}
		for i in range(1, len(nums)-1):
			for j in range(i+1, len(nums)):
				target = -nums[i]-nums[j]
				if target in seen:
					maybe.append([target, nums[i], nums[j]])
			seen.add(nums[i])
		out = []
		for m in maybe:
			if m not in out:
				out.append(m)
		return out

	def testfunc(self, nums: list[int]) -> list[list[int]]:
		return sorted(map(sorted, self.threeSum(nums)))

class SolutionSlow:
	def threeSum(self, nums: list[int]) -> list[list[int]]:
		maybe = []
		for i in range(len(nums)-2):
			for j in range(i+1, len(nums)-1):
				for k in range(j+1, len(nums)):
					if nums[i] + nums[j] + nums[k] == 0:
						maybe.append(sorted([nums[i], nums[j], nums[k]]))
		out = []
		for m in maybe:
			if m not in out:
				out.append(m)
		return out

	def testfunc(self, nums: list[int]) -> list[list[int]]:
		return sorted(map(sorted, self.threeSum(nums)))

def test(sol):
	test_cases = [
		([[-1, 0, 1, 2, -1, -4]], [[-1, -1, 2], [-1, 0, 1]]),
		([[0, 1, 1]], []),
		([[0, 0, 0]], [[0, 0, 0]]),
		([[0, 0, 0, 0]], [[0, 0, 0]]),
		([[-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]], [[-4, 0, 4], [-4, 1, 3], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, -1, 2], [-1, 0, 1]]),
	]
	for inp,out in test_cases:
		got = sol().testfunc(*inp)
		assert got == out, "threeSum(%s) = %s, want %s" % (inp, got, out)

if __name__ == "__main__":
	test(SolutionFast)
	test(Solution)
	test(SolutionSlow)
	from timeit import timeit
	print(timeit('test(SolutionFast)', globals=globals()))
	print(timeit('test(Solution)', globals=globals()))
	print(timeit('test(SolutionSlow)', globals=globals()))
