'''
date : 2018.10.22
author : 极简XksA 老表
'''
'''
题目：
	给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，
	判断字符串是否有效。
	注意空字符串可被认为是有效字符串。
'''

# 我的方法
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        reg_dict = {')':'(','}':'{',']':'['}
        # 括号匹配集
        temp_list = []
        # 临时存储栈
        for i in range(len(s)):
           if s[0] in reg_dict:
                return False
           if s[i] not in reg_dict: # 左括号，入栈
              temp_list.append(s[i])
           else:  # 右括号，取出栈顶，匹配
              if temp_list == []: # 有右括号无左括号可匹配
                 return False
              if not temp_list[-1] == reg_dict[s[i]]: # 左右括号不匹配
                 return False
              temp_list.pop()  # 匹配成功出栈
        if temp_list != []:
            return False
        return True
	           
			
class Solution1:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str0 = s
        while "{}" in str0 or "()" in str0 or "[]" in str0:
            str0 = self.replacebracket(str0)
        if str0 == "":
            return True
        return False
	       
    
    def replacebracket(self,str0):
        str0 = str0.replace("{}","")
        str0 = str0.replace("()","")
        str0 = str0.replace("[]","")
        return str0

s0 = Solution1()
str_00 = "[{]}"
result = s0.isValid(str_00)
print(result)