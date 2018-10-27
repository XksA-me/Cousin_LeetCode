'''
date : 2018.10.15
author : 极简XksA
'''
'''
题目：
	给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
	使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
'''

# 我的方法
class Solution1(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        first_num = 0
        second_num = 0
        third_num = 0
        res_list = []
        n_len = len(nums)
        nums.sort()
        # dict_nums = {nums[m]: m for m in range(len(nums))}
        pass_nums = []
        print(nums)
        for i in range(len(nums)):
            if nums[i] in pass_nums:
                  continue
            nums_1 = nums[i+1:n_len]
            pass_nums.append(nums[i])
            #print(nums_1)
            #print("nums_1---------------------------")
            dict_nums_1 = {nums_1[m]:m for m in range(len(nums_1))}
            index_0 = []
            for j in range(len(nums_1)):
                target = -(nums[i] + nums_1[j])
                # print(target)
                # print('target------------------------')
                if target in dict_nums_1:
                    if dict_nums_1[target] != j:
                        res_list.append([nums[i],nums_1[j],target])
                        pass_nums.append(nums_1[j])
                        pass_nums.append(target)
                        # print([nums[i],nums_1[j],target])
                        # print("---------------------------")

        return res_list

# class Solution(object):
#     def threeSum(self, nums):
#         """
# 		:type nums: List[int]
# 		:rtype: List[List[int]]
# 		"""
# 		# 列表排序，从小到大
# 		nums.sort()
# 		# [-4, -1, -1, 0, 1, 2]
# 		res_list = []
# 		# 头部循环查找
# 		for i in range(len(nums)):
# 			if i == 0 or nums[i] > nums[i - 1]:
# 				# 最左端
# 				l = i + 1
# 				# 最右端
# 				r = len(nums) - 1
# 				while l < r:  # 正在查找
# 					three_sum = nums[i] + nums[l] + nums[r]
# 					if three_sum == 0:
# 						res_list.append([nums[i], nums[l], nums[r]])
# 						l += 1 # 右移一位
# 						r -= 1 # 左移一位
# 						while l < r and nums[l] == nums[l - 1]:
# 							# 从左往右，相同数值直接跳过
# 							l += 1
# 						while r > l and nums[r] == nums[r + 1]:
# 							# 从右往左，相同数值直接跳过
# 							r -= 1
# 					elif three_sum > 0:
# 						# 大于零，右边数值大，左移
# 						r -= 1
# 					else:
# 						# 小于零，左边数值小，右移
# 						l += 1
# 		return res_list
  
  
class Solution2:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num_1=[]
        num_2=[]
        result=[]
        # 区分正负数
        for i in nums:
            if i>=0:
                num_1.append(i)
            else:
                num_2.append(i)

        for m,n in num_2:
            if abs(m+n) in num_1:
                result.append([m,n,abs(m+n)])
        return result

		       
s0 = Solution2()
nums = [-1, 0, 1, 2, -1,-4]
# [-4, -1, -1, 0, 1, 2]
res_list = s0.threeSum(nums)
print(res_list)