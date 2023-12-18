class Solution:
	def twoSum(self, nums: list[int], target: int) -> list[int]:
		idx = {}
		for i in range(len(nums)):
			other = target - nums[i]
			if other in idx:
				return [idx[other], i]
			idx[nums[i]] = i

class SolutionSlow:
	def twoSum(self, nums: list[int], target: int) -> list[int]:
		for i in range(len(nums)-1):
			for j in range(i+1, len(nums)):
				if nums[i] + nums[j] == target:
					return [i, j]

def test():
	test_cases = [
		([[2, 7, 11, 15], 9], [0, 1]),
		([[3, 2, 4], 6], [1, 2]),
		([[3, 3], 6], [0, 1]),
	]
	for inp,out in test_cases:
		got = Solution().twoSum(*inp)
		assert got == out, "twoSum(%s) = %s, want %s" % (inp, got, out)

if __name__ == "__main__":
	test()
