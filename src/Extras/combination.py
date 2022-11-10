#!/usr/bin/env python

def combinationSum(candidates, target):
    candidates.sort()
    output = []
    dfs(candidates, target, 0, [], output)
    return output

def dfs(candidates, target, index, path, output):
    if not target:
        output.append(path)
        return None
    for i in range(index, len(candidates)):
        if target < candidates[i]:
            break
        dfs(candidates, target-candidates[i], i, path+[candidates[i]], output)


if __name__ == '__main__':
    print(combinationSum([2,3,6,7], 7))