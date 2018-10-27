'''
date : 2018.9.23
author : 极简XksA
'''
'''
题目：
	给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。

	请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。

	你可以假设 nums1 和 nums2 不同时为空。
'''
# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         nums = nums1+nums2
#         nums.sort()
#         l = len(nums)
#         if l%2 == 0 :
#             index = [l//2 - 1,l//2]
#         else:
#             index = [l//2,l//2]
#         # 求中位数
#         median_num = (nums[index[0]]+nums[index[1]])/2
#         return median_num
#
# nums1 = [1,2]
# nums2 = [3,4]
# s0 = Solution()
# median_num = s0.findMedianSortedArrays(nums1,nums2)
# print(median_num)

# # 方法二
# # class Solution:
# #     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
# #         nums=[]
# #         len1=len(nums1)
# #         len2=len(nums2)
# #         num1=num2=0
# #         len0=len1+len2
# #         for i in range(len0):
# #             if(num1==len1):  # 列表nums1遍历完
# #                 nums.append(nums2[num2])
# #                 num2=num2+1
# #                 continue
# #             if(num2==len2): # 列表nums2遍历完
# #                 nums.append(nums1[num1])
# #                 num1=num1+1
# #                 continue
# #             if(nums1[num1]<=nums2[num2]):
# #                 nums.append(nums1[num1])
# #                 num1=num1+1
# #                 continue
# #             else:
# #                 nums.append(nums2[num2])
# #                 num2=num2+1
# #                 continue
# #         if(len0%2==0):
# #             return (nums[len0//2]+nums[len0//2-1])/2.0
# #         else:
# #             return nums[len0//2]
class Solution:
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    def find(self, nums1, s1, e1, nums2, s2, e2, k):
        if e1 - s1 < 0:
            return nums2[k + s2]
        if e2 - s2 < 0:
            return nums1[k + s1]
        if k < 1:
            return min(nums1[k + s1], nums2[k + s2])
        ia, ib = (s1 + e1) // 2 , (s2 + e2) // 2
        ma, mb = nums1[ia], nums2[ib]
        if (ia - s1) + (ib - s2) < k:
            if ma > mb:
                return self.find(nums1, s1, e1, nums2, ib + 1, e2, k - (ib - s2) - 1)
            else:
                return self.find(nums1, ia + 1, e1, nums2, s2, e2, k - (ia - s1) - 1)
        else:
            if ma > mb:
                return self.find(nums1, s1, ia - 1, nums2, s2, e2, k)
            else:
                return self.find(nums1, s1, e1, nums2, s2, ib - 1, k)
    def findMedianSortedArrays(self, nums1, nums2):
        l = len(nums1) + len(nums2)
        if l % 2 == 1: # 奇数
            return self.find(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, l // 2)
        else: # 偶数
            return (self.find(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, l // 2) + self.find(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, l // 2 - 1)) / 2.0

