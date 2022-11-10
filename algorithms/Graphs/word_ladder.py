#!/usr/bin/env python


from collections import defaultdict, deque


def word_ladder(begin_word, end_word, word_list):
    if end_word not in word_list:
        return 0
    word_list = set(word_list)
    q = [[begin_word, 1]]
    while q:
        word, length = q.pop(0)
        if word == end_word:
            return length
        for i in range(len(word)):
            for j in map(chr, range(ord('a'), ord('z')+1)):
                next_word = word[:i] + j + word[i+1:]
                if next_word in word_list:
                    word_list.remove(next_word)
                    q.append([next_word, length+1])
    return 0

def word_ladder2(begin_word, end_word, word_list):
    if end_word not in word_list:
        return []
    
    word_list = set(word_list)
    path = defaultdict(list)
    path[begin_word].append([begin_word])

    while path:
        new_path = defaultdict(list)
        for word in path:
            if word in end_word:
                return path[word]
            for i in range(len(word)):
                for j in map(chr, range(ord('a'), ord('z')+1)):
                    next_word = word[:i] + j + word[i+1:]
                    if next_word in word_list:
                        new_path[next_word] += [i + [next_word] for i in path[word]]
        word_list -= set(path.keys())
        path = new_path

    return []

if __name__ == '__main__':
    print(word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
    print(word_ladder2("hit", "cog", ["hot","dot","dog","lot","log","cog"]))