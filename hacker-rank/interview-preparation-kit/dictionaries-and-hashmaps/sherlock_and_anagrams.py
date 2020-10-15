def sherlock_and_anagrams(s):
    dict_anagrams = {}
    count_anagrams = 0

    for i in range(len(s)):
        for j in range(len(s)-i):
            w = ''.join(sorted(s[(j):(i+j+1)]))

            if w in dict_anagrams:
                count_anagrams += 1 + dict_anagrams[w]
                dict_anagrams[w] += 1
            else:
                dict_anagrams[w] = 0

    return count_anagrams


s = 'abba'  # 4
s = 'ifailuhkqq'  # 3
s = 'kkkk'  # 10
s = 'cdcd'  # 5

print(sherlock_and_anagrams(s))
