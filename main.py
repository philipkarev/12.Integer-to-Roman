class Solution:
    def intToRoman(self, num: int) -> str:

        # roman values
        rv = [['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', ''],
              ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', ''],
              ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM', ''],
              ['M', 'MM', 'MMM']]

        s = ''  # output string of roman number

        for i in range(len(str(num))):
            s = rv[i][int(list(str(num))[len(str(num)) - i - 1]) - 1] + s

        return s


def main():

    sol = Solution()
    print(sol.intToRoman(100))


main()