'''
date : 2018.10.18
author : 极简XksA
'''
'''
题目：
	给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
	找出 nums 中的三个整数，使得它们的和与 target 最接近。
	返回这三个数的和。假定每组输入只存在唯一答案。
'''

# 我的方法
# class Solution(object):
# 	def threeSumClosest(self, nums, target):
# 		"""
# 		:type nums: List[int]
# 		:type target: int
# 		:rtype: int
# 		"""
# 		# 距离
# 		distance_t = 10000
# 		# 返回结果
# 		result_sum = 0
# 		# 1.排序，方便比较
# 		nums.sort()
# 		# 一层：找出头
# 		for i in range(len(nums)-2):
# 			left = i + 1
# 			right = len(nums) - 1
# 			first = nums[i]
# 			# 二层：左右夹击
# 			while left < right:
# 				second = nums[left]
# 				third = nums[right]
# 				sum = first + second + third
# 				abs_flag = abs(sum - target)
# 				if abs_flag == 0: # 最接近
# 					return target
# 				elif abs_flag < distance_t: # 距离变小，记录当前sum和distance_t
# 					result_sum = sum
# 					distance_t = abs_flag
# 				if sum > target:
# 					right -= 1   # 左移变大
# 				else:
# 					left += 1    # 右移变小
# 		return result_sum

# 大牛方法
class Solution(object):
	def threeSumClosest(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		nums.sort()
		length = len(nums)
		closest = []
		
		for i, num in enumerate(nums[0:-2]):
			l, r = i + 1, length - 1
			
			# different with others' solution
			
			if num + nums[r] + nums[r - 1] < target:
				closest.append(num + nums[r] + nums[r - 1])
			elif num + nums[l] + nums[l + 1] > target:
				closest.append(num + nums[l] + nums[l + 1])
			else:
				while l < r:
					closest.append(num + nums[l] + nums[r])
					if num + nums[l] + nums[r] < target:
						l += 1
					elif num + nums[l] + nums[r] > target:
						r -= 1
					else:
						return target
		
		closest.sort(key=lambda x: abs(x - target))
		return closest[0]

nums =[1,2,4,8,16,32,64,128]

target = 82
s0 = Solution()
result = s0.threeSumClosest(nums,target)
print(result)
				

