class Solution:
    def myAtoi(self, s: str) -> int:
        idx, sign, res = 0, 1, 0

        s = s.lstrip()

        if idx < len(s) and s[idx] in "+-":
            if s[idx] == "-":
                sign = -1
            idx += 1

        while idx < len(s) and s[idx].isdigit():
            res = res * 10 + int(s[idx])
            idx += 1

        res *= sign

        if res < -(2 ** 31):
            return -(2 ** 31)

        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1

        return res