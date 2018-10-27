'''
date : 2018.10.02
author : 极简XksA
'''
'''
题目：
	给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
'''

# 方法一
# class Solution:
# 	def longestPalindrome(self, s):
# 		"""
# 		:type s: str
# 		:rtype: str
# 		"""
# 		len_s = len(s)
# 		if len_s == 1:
# 			return s
# 		substring = ''
# 		substring_set = []
# 		for i in range(len_s):
# 			for j in range(len_s):
# 				if i < j :
# 					substring = s[i:j+1]
# 					if self.is_Palindrome(substring) == 1:
# 						# sub_dict = {"str":"","len":0}
# 						# sub_dict = {}
# 						# sub_dict[substring] = len(substring)  # j-i+1
# 						substring_set.append(substring)
# 		longest_s = ''
# 		if substring_set:
# 			longest_s = substring_set[0]
# 		else:
# 			return s[0]
# 		for i in range(len(substring_set) - 1):
# 			if len(longest_s) < len(substring_set[i + 1]):
# 				longest_s = substring_set[i + 1]
# 		return longest_s
#
# 	def is_Palindrome(self,str_t):
# 		len_t = len(str_t)
# 		for i in range(len_t):
# 			if not str_t[i] == str_t[len_t - 1 - i]:
# 				return 0
# 		return 1
# import time
# start_time = time.time()
# s = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
# print(len(s))
#
# s0 = Solution()
# l_Palindrome = s0.longestPalindrome(s)
# print(l_Palindrome)
# end_time = time.time()
# print(end_time - start_time)

# 方法二
# class Solution:
# 	# 类变量，类全局可调用
# 	longest_s = ''  # 最长回文字符串
# 	maxLen = 0  # 长度
#
# 	def longestPalindrome(self, s):
# 		"""
# 		:type s: str
# 		:rtype: str
# 		"""
# 		len_s = len(s)
# 		if len_s == 1:  # 单字符串
# 			return s
# 		for i in range(len_s):
# 			# 单核(奇数向两边延伸)
# 			self.find_longest_Palindrome(s, i, i)
# 			# 双核（偶数向两边延伸）
# 			self.find_longest_Palindrome(s, i, i + 1)
# 		return self.longest_s
#
# 	# 找出最长的回文字符串
# 	def find_longest_Palindrome(self, s, low, high):
# 		# 从中间向两端延伸，判断是否为回文字符串的同时寻找最长长度
# 		while low >= 0 and high < len(s):
# 			if s[low] == s[high]:
# 				low -= 1  # 向左延伸
# 				high += 1  # 向右延伸
# 			else:
# 				break
# 		# high - low - 1 表示当前回文字符串长度
# 		if high - low - 1 > self.maxLen:
# 			self.maxLen = high - low - 1
# 			self.longest_s = s[low + 1:high]

# 方法三
class Solution:
	s_new = ''
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		t0 = '#'.join(s)
		s_new = '#' + t0 + '#'
		len_new = []
		sub = '' # 最长回文字符串
		sub_midd = 0  # 表示在i之前所得到的Len数组中的最大值所在位置
		sub_side = 0  # 表示以sub_midd为中心的最长回文子串的最右端在S_new中的位置
		for i in range(len(s_new)):
			if i < sub_side :
				# i < sub_side时，在Len[j]和sub_side - i中取最小值，省去了j的判断
				j = 2 * sub_midd - i
				if j >= 2 * sub_midd - sub_side and  len_new[j] <= sub_side - i:
					len_new.append(len_new[j])
				else:
					len_new.append(sub_side - i + 1)
			else:
				# i >= sub_side时，从头开始匹配
				len_new.append(1)
			while ((i - len_new[i] >= 0 and i + len_new[i] < len(s_new)) and (s_new[i - len_new[i]] == s_new[i + len_new[i]])):
				# s_new[i]两端开始扩展匹配，直到匹配失败时停止
				len_new[i] = len_new[i] + 1
				
			if len_new[i] >= len_new[sub_midd]:
				sub_side = len_new[i] + i - 1
				sub_midd = i
		a0 = int((2 * sub_midd - sub_side)/2)
		b0 = int(sub_side / 2)
		sub = s[a0 :b0 ] # 在s中找到最长回文子串的位置
		return sub
import time
start_time = time.time()
s = "cbcbb"
print(len(s))

s0 = Solution()
l_Palindrome = s0.longestPalindrome(s)
print(l_Palindrome)
end_time = time.time()
# print(end_time - start_time)