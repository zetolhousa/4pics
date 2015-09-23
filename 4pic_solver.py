#!/usr/bin/env python3
import itertools

length = int(input("Enter length of word: "))
characters = input("Enter the characters given: ")

def combinator(characters, length):
    perms = []
    for p in itertools.combinations(characters, length):    #replaced permut with combin
        res = ''.join(p)   #returns a tuple
        perms.append(res)
    return perms

with open('/home/tlhousa/Downloads/eng_words/words2.txt') as words:
    for word in words:
        l = len(word)-1
        if length == l:
            for c in combinator(characters, length):
                s1 = list(c)
                s2 = list(word.rstrip())
                s1.sort()
                s2.sort()
                if s1 == s2:
                    print(word)
