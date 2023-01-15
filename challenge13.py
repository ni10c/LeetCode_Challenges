class Solution(object):
    def romanToInt(self, s):
        ROMAN_DICT = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        
        total = 0
        prev = 0
        for i in range(len(s)):
            # print(i)
            curr = ROMAN_DICT[s[i]]
            # print(curr)
            if curr > prev:
                # print(curr - 2 * prev)
                total += curr - 2 * prev
                # print(total)
            else:
                total += curr
                # print(total)
            prev = curr
        print(total)
        return total
    def superbowl(self, s):
        ROMAN_DICT = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        
        total = 0
        prev = 0
        for i in range(len(s)):
            # print(i)
            curr = ROMAN_DICT[s[i]]
            # print(curr)
            if curr > prev:
                # print(curr - 2 * prev)
                total += curr - 2 * prev
                # print(total)
            else:
                total += curr
                # print(total)
            prev = curr
        print(f"This Year is Super Bowl {total}!")
        return total

Solution.romanToInt(Solution,s = "III")
Solution.romanToInt(Solution,s = "LVIII")
Solution.romanToInt(Solution,s = "MCMXCIV")
Solution.superbowl(Solution,s = "LVII")
