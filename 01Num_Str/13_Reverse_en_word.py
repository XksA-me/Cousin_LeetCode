'''
date : 2018.11.7
author : 极简XksA
'''
'''
题目：
	给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
注意：
	在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
'''


class Solution(object):
	def reverseWords(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		# 根据空格，把字符串分隔开
		r_list = s.split(" ")
		
		# 把列表每个单词字符串逆转
		for i in range(len(r_list)):
			r_list[i] = r_list[i][::-1]
		
		# 用 “ ” 连接列表的每个单词
		result_s = " ".join(r_list)
		
		return result_s


class Solution1(object):
	def reverseWords(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		# 根据空格，把字符串分隔开
		s = s + ' '
		r_list = []
		word = ''
		flag = 0
		for i in s:
			if i != " ":
				word = word + i
				flag = 1
			else:
				if flag == 1:
					r_list.append(word)
					word = ''
					flag = 0
		
		# 把列表每个单词字符串逆转
		for i in range(len(r_list)):
			r_list[i] = self.reverseString(r_list[i])
			
		# 用 “ ” 连接列表的每个单词
		result_s = ''
		for i in range(len(r_list)):
			if i == len(r_list)-1:
				result_s = result_s + r_list[i]
				break
			result_s = result_s + r_list[i] + " "
		
		return result_s
	
	# leetcode12中自己实现字符串逆转
	def reverseString(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		result = list(s)
		for i in range(len(result)//2):
			temp = result[len(result)-i-1]
			result[len(result)-i-1] = result[i]
			result[i] = temp
		return ''.join(result)
	
s0 = Solution1()
str0 = "hehe hehe hehe hehe"
t0 = s0.reverseWords(str0)
print(t0)
