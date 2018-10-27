'''
date : 2018.10.24
author : 极简XksA
'''
'''
题目：
	给定一个排序数组，你需要在原地删除重复出现的元素，
	使得每个元素只出现一次，返回移除后数组的新长度。
	不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
'''


# 我的方法
class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		if n<=0:  # 长度小于或等于1
			return 0
		len_0 = 1
		for i in range(1,n): # for循环向后遍历
			if nums[i] != nums[i-1]:
				nums[len_0] = nums[i]  # 数据替换
				len_0 = len_0 + 1 # 指针后移
		return len_0

from collections import OrderedDict
class Solution1(object):
   def removeDuplicates(self, nums):
        nums[:] =  OrderedDict.fromkeys(nums).keys()
        return len(nums)


class Solution2(object):
	def removeDuplicates(self, nums):
		
		if not nums:
			return 0
		lastUniqIdx = 0
		for i in range(len(nums)):
			if nums[i] > nums[lastUniqIdx]:
				lastUniqIdx += 1
				nums[lastUniqIdx] = nums[i]
		return lastUniqIdx + 1

class Solution3():
	def removeDuplicates(self,nums):
		nums[:] = list(sorted(set(nums)))
		return len(nums)
s0 = Solution3()
nums = [1,1,3]
result = s0.removeDuplicates(nums)
print(nums)
print(result)
