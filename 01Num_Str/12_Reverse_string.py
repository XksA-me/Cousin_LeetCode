'''
date : 2018.11.5
author : 极简XksA
'''
'''
题目：
	编写一个函数，其作用是将输入的字符串反转过来。
'''


class Solution(object):
	def reverseString(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		return s[::-1]

class Solution1(object):
	def reverseString(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		from functools import reduce
		return reduce(lambda x,y:y+x,s)

class Solution2(object):
	def reverseString(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		s = list(s)
		return "".join(reversed(s))
	
class Solution3(object):
	def reverseString(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		if len(s) < 1:
			return s
		return self.reverseString(s[1:]) + s[0]

class Solution4(object):
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
	
	
# re.compile()
s0 = Solution4()
str0 = "hellof"
t0 = s0.reverseString(str0)
print(t0)
