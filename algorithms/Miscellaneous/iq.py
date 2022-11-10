#!/usr/bin/env python


def unique_charecters(str):
    str_dict = {}
    for char in str:
        if char in str_dict:
            return False
        str_dict[char] = 1
    return True

def main():
    unique_charecters('abvsada')
    unique_charecters('abcdegh')


if __name__ == '__main__':
    main()