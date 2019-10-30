class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1

        if digits[-1] < 10:
            return digits

        i = len(digits) - 1
        while i >= 0:
            if digits[i] > 9:
                digits[i] = 0
                if i == 0:
                    break
                digits[i - 1] += 1
            i -= 1

        if digits[0] == 0:
            digits[0] = 1
            digits[:] += [0]
        return digits



