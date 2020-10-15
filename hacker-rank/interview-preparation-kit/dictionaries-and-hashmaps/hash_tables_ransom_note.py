def ransom_note(magazine, note):
    dict_magazine = {}

    for m in magazine:
        if m not in dict_magazine:
            dict_magazine[m] = 1
        else:
            dict_magazine[m] += 1

    check = True

    for n in note:
        if n in dict_magazine:
            dict_magazine[n] -= 1
            if dict_magazine[n] == 0:
                del dict_magazine[n]
        else:
            check = False
            break

    if check:
        print('Yes')
    else:
        print('No')


magazine = ['give', 'me', 'one', 'grand', 'today', 'night']
note = ['give', 'one', 'grand', 'today']

# magazine = ['two', 'times', 'three', 'is', 'not', 'four']
# note = ['two', 'times', 'two', 'is', 'four']

# magazine = ['ive', 'got', 'a', 'lovely', 'bunch', 'of', 'coconuts']
# note = ['ive', 'got', 'some', 'coconuts']

ransom_note(magazine, note)
