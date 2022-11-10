#!/usr/bin/env python

class LCS:
    def __init__(self) -> None:
        self.lcs_dict = {}

    def lcs(self, x, y):
        """!
        lcs without recursion using 2d Lookup array.
        """
        max_len, prev = 0, [0]*(len(y)+1)
        for i in range(1, len(x)+1):
            curr = [0]*(len(y)+1)
            for j in range(1, len(y)+1):
                if x[i-1] == y[j-1]:
                    curr[j] = prev[j-1] + 1
                else:
                    curr[j] = max(curr[j-1], prev[j])
                max_len = max(max_len, curr[j])
            prev = curr

        return max_len

    def lcs_through_recursion(self, x, y, len_x, len_y):
        "Complexity is 2^n so not advisable"
        if not len_x or not len_y:
            return 0
        elif x[len_x-1] == y[len_y-1]:
            return 1 + self.lcs_through_recursion(x, y, len_x-1, len_y-1)
        else:
            return max(self.lcs_through_recursion(x, y, len_x-1, len_y),
                       self.lcs_through_recursion(x, y, len_x, len_y-1))

if __name__ == '__main__':
    lcs_obj = LCS()
    x = 'GXTXAYB'
    y = 'AGGTAB'
    print('Length of LCS is ', lcs_obj.lcs(x , y))
    print('Length of LCS is ', lcs_obj.lcs_through_recursion(x , y, len(x), len(y)))
