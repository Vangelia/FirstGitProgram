# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def match_ends(words):
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count

def front_x(words):
    tlist = []
    commonlist = []
    for word in words:
        if word[0] == 't':
            tlist.append(word)
        else:
            commonlist.append(word)
    return sorted(tlist) + sorted(commonlist)

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
    print
    'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print
    'front_x'
    test(front_x(['bbb', 'ccc', 'att', 'tzz', 'taa']),
         ['taa', 'tzz', 'att', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'tcc', 'taa']),
         ['taa', 'tcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['test', 'xyz', 'python', 'language', 'table']),
         ['table', 'test', 'language', 'python', 'xyz'])

    print
    print
    'sort_last'
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    main()

