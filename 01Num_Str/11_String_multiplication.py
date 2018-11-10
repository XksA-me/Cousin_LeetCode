'''
date : 2018.10.31
author : 极简XksA
'''
'''
题目：
	给定两个以字符串形式表示的非负整数 num1 和 num2，
	返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
'''

# 这种方法适用于工作，不适和面试
class Solution(object):
	def multiply(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		num1 = int(num1)
		num2 = int(num2)
		result = num1*num2
		return result

#
class Solution1(object):
	def multiply(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		# 设置存储列表(原理见思路分析)
		product = [0] * (len(num1) + len(num2))
		# 下标
		pos = len(product) - 1
		# 字符串逆转，方便从个位开始遍历
		num1 = num1[::-1]
		num2 = num2[::-1]
		# 遍历被乘数字符串
		for n1 in num1:
			# 数据存储位置(数量级，第一次个位相乘，最后一位，第二次十位相乘，倒数第二位...)
			tempPos = pos
			# 遍历乘数字符串
			for n2 in num2:
				# 单个数据相乘
				product[tempPos] += int(n1) * int(n2)
				# 取十位及以上量级
				product[tempPos - 1] += product[tempPos] // 10
				# 取个位
				product[tempPos] %= 10
				# 前移
				tempPos -= 1
			# 前移，增加数量级
			pos -= 1
		# 找到结果列表非零数
		pt = 0
		while pt < len(product) - 1 and product[pt] == 0:
			pt += 1
		# 切片取出数据
		res_list = product[pt:]
		# map转换成迭代对象，用jion函数连接返回
		return ''.join(map(str,res_list))

s0 = Solution1()
num1 = "12"
num2 = "23"
result = s0.multiply(num1,num2)
print(result)