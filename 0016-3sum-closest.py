class Solution:
	def threeSumClosest(self, nums: list[int], target: int) -> int:
		closest = float("inf")
		nums.sort()
		for i in range(len(nums)-2):
			j = i+1
			k = len(nums)-1
			while j < k:
				s = nums[i] + nums[j] + nums[k]
				if abs(target-s) < abs(target-closest):
					closest = s
				if s < target:
					j += 1
					while j < k and nums[j] == nums[j-1]:
						j += 1
				elif s > target:
					k -= 1
					while j < k and nums[k] == nums[k+1]:
						k -= 1
				else:
					return s
		return closest

class SolutionSlow:
	def threeSumClosest(self, nums: list[int], target: int) -> int:
		closest = float("inf")
		for i in range(len(nums)-2):
			for j in range(i+1, len(nums)-1):
				for k in range(j+1, len(nums)):
					s = nums[i] + nums[j] + nums[k]
					if abs(target-s) < abs(target-closest):
						closest = s
		return closest

def test(sol):
	test_cases = [
		([[-1, 2, 1, -4], 1], 2),
		([[0, 0, 0], 1], 0),
	]
	for inp,out in test_cases:
		got = sol().threeSumClosest(*inp)
		assert got == out, "threeSumClosest(%s) = %s, want %s" % (inp, got, out)

if __name__ == "__main__":
	test(Solution)
	test(SolutionSlow)
	from timeit import timeit
	print(timeit('test(Solution)', globals=globals()))
	print(timeit('test(SolutionSlow)', globals=globals()))
