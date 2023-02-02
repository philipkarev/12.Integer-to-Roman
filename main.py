class Solution:
    def intToRoman(self, num: int) -> str:

        # roman values
        rv = [['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', ''],
              ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', ''],
              ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM', ''],
              ['M', 'MM', 'MMM']]

        s = ''  # output string of roman number

        strnum = str(num)
        lensn = len(strnum)
        listsn = list(strnum)

        for i in range(lensn):
            s = rv[i][int(listsn[lensn - i - 1]) - 1] + s

        return s


def main():

    sol = Solution()
    print(sol.intToRoman(100))


main()