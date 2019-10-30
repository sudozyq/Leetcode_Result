class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        result = []
        for i in nums1:
            for j in nums2:
                if i ^ j == 0:
                    result.append(i)
                    nums2.remove(i)
                    break

        return result
