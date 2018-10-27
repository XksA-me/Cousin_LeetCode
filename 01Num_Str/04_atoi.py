'''
date : 2018.10.08
author : 极简XksA
'''
'''
题目：
	实现 atoi，将字符串转为整数。
	ascii to integer
'''

# 我的方法
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
	    # 字符串不为空/第一个字符不为数字/-/+
        str = str.strip()  # 去除两端空格
        if str == '':   #为空
	        return 0
        if str[0] != '-' and str[0] != '+' and not str[0].isdigit():
            return 0    # 第一个字符不为数字/-/+
        import re
        # 确保字符串内包含数字/+/-
        pattern = re.compile("[-+0-9]+")
        judge = pattern.findall(str)
        # 例如：" ","-","+"
        if not judge or judge[0] == '+' or judge[0] == '-':
              return 0
        # 例如："++","--","-+/+-","-2-","2-","--2"
        if len(judge[0]) >=  2:
	        # 确保字符串内包含数字
            pattern0 = re.compile("[0-9]+")
            test01 = pattern0.findall(judge[0])
            if not test01:
                return 0  # 只有+/-
            if not judge[0][1:2].isdigit():
                return 0   #去除  ++/-- 属于第一个字符不为数字情况
            if judge[0][0] == '-' or judge[0][0] == '+':
                judge[0] = judge[0][0] + test01[0]   # 第一个字符为 +/- 结果为符号+数字
            else:  # 只有数字，无符号位
                judge[0] = test01[0]
        interim_target = float(judge[0])  # 转换成float判断范围
        if interim_target < -2147483648:
            return -2147483648
        if interim_target > 2147483647:
            return 2147483647
        target = int(judge[0])  # 范围内，转换成int 返回
        return target
			
if 1== 1:
	pass
else:
	1
s0 = Solution()
str_t = "+-2"
result = s0.myAtoi(str_t)
print(result)