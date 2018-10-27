'''
date : 2018.9.22
author : 极简XksA
'''
'''
题目：
	给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
	你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
'''
# # 方法一：双重for循环
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         l = len(nums)
#         for a in range(l):
#             for b in range(l):
#                 if a != b:
#                     if nums[a]+nums[b] == target:
#                         return [a,b]
# nums = [2, 7, 11, 15]
# target = 9
# test_o = Solution()
# result = test_o.twoSum(nums,target)
# print(result)
# 方法二：改良双重for循环
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         # flags = [0 for i in range(len(nums))]
#         # l = len(nums)
#         # for a in range(l):
#         #     flags[a]=1
#         #     for b in range(l):
#         #         if flags[b]==0:
#         #             if nums[a]+nums[b] == target:
#         #                 return [a,b]
#         l = len(nums)
#         for a in range(l):
#            for b in range(a+1,l):
#               if nums[a] + nums[b] == target:
#                    return [a, b]
# nums = [2, 5, 3, 1]
# target = 4
# test_o = Solution()
# result = test_o.twoSum(nums,target)
# print(result)

# 方法三：一层循环
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         l = len(nums)
#         for a in range(l):
#             one_unm = nums[a]
#             other_one = target - one_unm
#             if other_one in nums:
# 	            b = nums.index(other_one)
# 	            if a != b:
# 		            if a>b:
# 		                return [b,a]
# 		            return [a,b]
# 	            pass
#
# nums = [2, 5, 3, 3]
# target = 6
# test_o = Solution()
# result = test_o.twoSum(nums,target)
# print(result)

# 方法四：一层for循环优化
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        flags = [0 for i in range(len(nums))]
        l = len(nums)
        dict_nums = {nums[i]:i for i in range(l)}
        print(dict_nums)
        for a in range(l):
            one_unm = nums[a]
            other_one = target - one_unm
            if other_one in dict_nums and a!= dict_nums[other_one]:
	            return [a,dict_nums[other_one]]
#
# nums = [3, 3, 1, 2]
# target = 6
# test_o = Solution()
# result = test_o.twoSum(nums,target)
# print(result)
# 方法五：元组实现
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         l = len(nums)
#         tuple_nums = tuple(nums)
#         for a in range(l):
#             one_unm = tuple_nums[a]
#             other_one = target - one_unm
#             if other_one in tuple_nums:
#                 b = tuple_nums.index(other_one)
#                 if a!= b:
# 	                return [a,b]
#
# nums = [3, 3, 1, 2]
# target = 6
# test_o = Solution()
# result = test_o.twoSum(nums,target)
# print(result)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_hash = {}
        enum_t = enumerate(nums)
        for index,number in enum_t:
            one_num = nums[index]
            other_num = target-one_num
            if other_num in nums_hash:
                return [nums_hash[other_num],index]
            nums_hash[number] = index
        return []

nums = [1, 3, 4, 2]
target = 5
test_o = Solution()
result = test_o.twoSum(nums,target)
print(result)