class Solution:
    def intToRoman(self, num: int) -> str:

        num = str(num)

        s = ''

        if num[len(num) - 1] == '1':
            s = 'I'
        elif num[len(num) - 1] == '2':
            s = 'II'
        elif num[len(num) - 1] == '3':
            s = 'III'
        elif num[len(num) - 1] == '4':
            s = 'IV'
        elif num[len(num) - 1] == '5':
            s = 'V'
        elif num[len(num) - 1] == '6':
            s = 'VI'
        elif num[len(num) - 1] == '7':
            s = 'VII'
        elif num[len(num) - 1] == '8':
            s = 'VIII'
        elif num[len(num) - 1] == '9':
            s = 'IX'

        if len(num) >= 2:
            if num[len(num) - 2] == '1':
                s = 'X' + s
            elif num[len(num) - 2] == '2':
                s = 'XX' + s
            elif num[len(num) - 2] == '3':
                s = 'XXX' + s
            elif num[len(num) - 2] == '4':
                s = 'XL' + s
            elif num[len(num) - 2] == '5':
                s = 'L' + s
            elif num[len(num) - 2] == '6':
                s = 'LX' + s
            elif num[len(num) - 2] == '7':
                s = 'LXX' + s
            elif num[len(num) - 2] == '8':
                s = 'LXXX' + s
            elif num[len(num) - 2] == '9':
                s = 'XC' + s

        if len(num) >= 3:
            if num[len(num) - 3] == '1':
                s = 'C' + s
            elif num[len(num) - 3] == '2':
                s = 'CC' + s
            elif num[len(num) - 3] == '3':
                s = 'CCC' + s
            elif num[len(num) - 3] == '4':
                s = 'CD' + s
            elif num[len(num) - 3] == '5':
                s = 'D' + s
            elif num[len(num) - 3] == '6':
                s = 'DC' + s
            elif num[len(num) - 3] == '7':
                s = 'DCC' + s
            elif num[len(num) - 3] == '8':
                s = 'DCCC' + s
            elif num[len(num) - 3] == '9':
                s = 'CM' + s

        if len(num) == 4:
            if num[0] == '1':
                s = 'M' + s
            if num[0] == '2':
                s = 'MM' + s
            if num[0] == '3':
                s = 'MMM' + s

        return s


def main():

    print("Enter valid integer number in range [1, 3999]:")

    num = input()
    num = int(num)

    num = str(num)

    s = ''

    if num[len(num) - 1] == '1':
        s = 'I'
    elif num[len(num) - 1] == '2':
        s = 'II'
    elif num[len(num) - 1] == '3':
        s = 'III'
    elif num[len(num) - 1] == '4':
        s = 'IV'
    elif num[len(num) - 1] == '5':
        s = 'V'
    elif num[len(num) - 1] == '6':
        s = 'VI'
    elif num[len(num) - 1] == '7':
        s = 'VII'
    elif num[len(num) - 1] == '8':
        s = 'VIII'
    elif num[len(num) - 1] == '9':
        s = 'IX'

    if len(num) >= 2:
        if num[len(num) - 2] == '1':
            s = 'X' + s
        elif num[len(num) - 2] == '2':
            s = 'XX' + s
        elif num[len(num) - 2] == '3':
            s = 'XXX'  + s
        elif num[len(num) - 2] == '4':
            s = 'XL' + s
        elif num[len(num) - 2] == '5':
            s = 'L' + s
        elif num[len(num) - 2] == '6':
            s = 'LX' + s
        elif num[len(num) - 2] == '7':
            s = 'LXX' + s
        elif num[len(num) - 2] == '8':
            s = 'LXXX' + s
        elif num[len(num) - 2] == '9':
            s = 'XC' + s

    if len(num) >= 3:
        if num[len(num) - 3] == '1':
            s = 'C' + s
        elif num[len(num) - 3] == '2':
            s = 'CC' + s
        elif num[len(num) - 3] == '3':
            s = 'CCC' + s
        elif num[len(num) - 3] == '4':
            s = 'CD' + s
        elif num[len(num) - 3] == '5':
            s = 'D' + s
        elif num[len(num) - 3] == '6':
            s = 'DC' + s
        elif num[len(num) - 3] == '7':
            s = 'DCC' + s
        elif num[len(num) - 3] == '8':
            s = 'DCCC' + s
        elif num[len(num) - 3] == '9':
            s = 'CM' + s

    if len(num) == 4:
        if num[0] == '1':
            s = 'M' + s
        if num[0] == '2':
            s = 'MM' + s
        if num[0] == '3':
            s = 'MMM' + s

    print(s)


main()