class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        index_IV = self.finder('IV', s)
        index_IX = self.finder('IX', s)
        index_XL = self.finder('XL', s)
        index_XC = self.finder('XC', s)
        index_CD = self.finder('CD', s)
        index_CM = self.finder('CM', s)
        numI = s.count('I')
        numV = s.count('V')
        numX = s.count('X')
        numL = s.count('L')
        numC = s.count('C')
        numD = s.count('D')
        numM = s.count('M')
        sum = numI + numV * 5 + numX * 10 + numL * 50 + numC * 100 + numD * 500 + numM * 1000
        if index_IV:
            sum -= 2
        if index_IX:
            sum -= 2
        if index_XL:
            sum -= 20
        if index_XC:
            sum -= 20
        if index_CD:
            sum -= 200
        if index_CM:
            sum -= 200
        return sum

    def finder(self, roman, s):
        """
        :type roman: str
        :rtype: boolean
        """
        return roman in s

