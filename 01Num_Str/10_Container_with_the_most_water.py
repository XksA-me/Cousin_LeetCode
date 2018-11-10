'''
date : 2018.10.30
author : 极简XksA
'''
'''
题目：
	给定n个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
	在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai)和(i, 0)。
	找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
'''


class Solution(object):
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		# 夹逼方法
		l = 0  # 左指针
		r = len(height) - 1   # 右指针
		max_area = 0
		while l < r:
			width = r-l  # 取矩形宽
			# 取矩形高
			if height[l] < height[r]:  # 右边高，以左边为高
					h = height[l]
					l += 1  # 左指针右移，找更高的高
			else:
					h = height[r]
					r -= 1  # 右指针左移，找更高的高
			# 取最大面积
			max_area = max(max_area, h * width)
		return max_area

# 简化代码
class Solution1(object):
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		# 快速复制
		l, r, max_value, tmp = 0, len(height) - 1, 0, 0
		while l < r :
			tmp = min(height[l], height[r]) * (r - l)
			max_value = max(tmp, max_value)
			if min(height[l], height[r]) == height[l]:
				l += 1 # 右移
			else:
				r -= 1 # 左移
		return max_value
	
	
s0 = Solution1()
list_0 = [1,8,6,2,5,4,8,3,7]
result = s0.maxArea(list_0)
print(result)