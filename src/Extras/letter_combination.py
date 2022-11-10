#!/usr/bin/env python
        
def letter_combinations(digits):
    num_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if not digits:
        return []

    output = []
    dfs(digits, 0, '', output, num_dict)
    return output

def dfs(digits, index, path, output, num_dict):
    if len(digits) == len(path):
        output.append(path)
        return None
    for i in range(index, len(digits)):
        for j in num_dict[digits[i]]:
            dfs(digits, i+1, path+j, output, num_dict)

        
if __name__ == '__main__':
    print(letter_combinations("23"))