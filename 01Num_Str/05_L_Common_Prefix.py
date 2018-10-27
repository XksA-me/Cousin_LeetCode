'''
date : 2018.10.11
author : 极简XksA
'''
'''
题目：
最长公共前缀
	编写一个函数来查找字符串数组中的最长公共前缀。
	如果不存在公共前缀，返回空字符串 ""。
	Longest Common Prefix
'''

# 我的方法
# class Solution:
# 	def longestCommonPrefix(self, strs):
# 		"""
# 		:type strs: List[str]
# 		:rtype: str
# 		"""
# 		len0 = len(strs)
# 		if len0 == 0:
# 			return ''
# 		list_len = []
# 		# 找出最短的字符串长度
# 		for i in range(len0):
# 			list_len.append(len(strs[i]))
# 		list_len.sort()
# 		# 取出最短的子串
# 		# 我这里是直接取第一个子串的前min_len
# 		com_str = strs[0][0:list_len[0]]
# 		b0 = com_str
# 		for s in strs:
# 			for i in range(list_len[0]):
# 				if s[i] != com_str[i]:
# 					# 判断到有不等的地方
# 					a0 = s[0:i]
# 					if len(b0) >= len(a0):  # 上一个最长公共前缀是否比现在长
# 						b0 = a0
# 		return b0
#

class Solution:
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		res = ""
		if len(strs) == 0:
			return ""
		# zip()函数用于将可迭代对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
		for each in zip(*strs):
			# 利用集合创建一个无序不重复元素集
			if len(set(each)) == 1:
				res += each[0]
			else:
				return res
		return res



s0 = Solution()
list_0 = ["a","aba","aaab"]
result = s0.longestCommonPrefix(list_0)
print(result)