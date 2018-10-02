#  1)listToString():


def listToString(a):
    assert isinstance(a, list), "a - Это не список!"
    a = str(a)
    assert isinstance(a, str), "И не строка!"
    return a

if __name__ == '__main__':
    def test_listStrings():
        assert listToString([]) == "[]", 'Test1 fail!'
        assert listToString([1, 2, 3]) == "[1, 2, 3]", 'Test2 fail!'
        assert listToString([-5]) == "[-5]", 'Test3 fail!'

        test_listStrings()

##############################################################################

#  2)addBorder()


def addBorder(a):
    Up_Down_Border = '+' + '-'*len(a[0]) + '+'  # Генерим крышу и пол
    new_list = list(map(lambda x: '|' + x + '|', a))  # Строим стены
    new_list.insert(0, Up_Down_Border)  # Строим крышу
    new_list.append(Up_Down_Border)  # Строим пол
    return new_list

if __name__ == '__main__':
    def test_addBorder():
        assert addBorder(['abc',
                          'def']) == ['+---+',
                                      '|abc|',
                                      '|def|',
                                      '+---+'], 'Test fail!'

    test_addBorder()

##############################################################################

#  3)shorting()


def shorting(e):
    new_list = list(map(lambda x: x if len(x) <= 10
                        else x[0] + str(len(x)-2) + x[-1], e))
    return new_list

if __name__ == '__main__':
    def test_shorting():
        assert shorting(['word',
                         'localization',
                         'internationalization',
                         'pneumonoultramicroscopicsilicovolcanoconiosis']) == [
              'word', 'l10n', 'i18n', 'p43s'], 'Test1 fail!'

    test_shorting()

##############################################################################

#  4)competition():


def competition(e, k):
    assert isinstance(e, list), "e - Это не список!"
    new_list = e[0:-k]
    min_score = e[-k-1]
    count_min_participants = e.count(min_score)
    if count_min_participants == 1:
        return len(new_list)
    else:
        return len(new_list)+count_min_participants-1

if __name__ == '__main__':
    def test_competition():
        assert competition([5, 4, 3, 2, 1], 2) == 3, 'Test1 fail!'
        assert competition([1, 0, 0, 0], 3) == 1, 'Test2 fail!'
        assert competition([10, 9, 8, 7, 7, 7, 5, 5], 4) == 6, 'Test3 fail!'

    test_competition()

##############################################################################

#  5)goodPairs()


def goodPairs(a, b):
    assert isinstance(a, list), "a - Это не список!"
    assert isinstance(b, list), "b - Это не список!"
    new_list = []
    for i in a:
        for j in b:
            if (i*j) % (i+j) == 0:
                new_list.append(i**2+j**2)
    return new_list

if __name__ == '__main__':
    def test_goodPairs():
        assert goodPairs([4, 5, 6, 7, 8], [8, 9, 10, 11, 12]) == [
                128, 160, 180], 'Test1 fail!'
        assert goodPairs([2], [2]) == [8], 'Test2 fail!'
        assert goodPairs([7, 8, 9], [5, 3, 2]) == [], 'Test3 fail!'

    test_competition()

##############################################################################

#  6)makeShell()


def makeShell(e):
    new_list = []
    counter = 1
    while counter <= e:
        new_list.append([0 for i in range(counter)])
        counter += 1
    counter -= 2
    while counter > 0:
        new_list.append([0 for i in range(counter)])
        counter -= 1
    return new_list


if __name__ == '__main__':
    def test_makeShell():
        assert makeShell(1) == [[0]], 'Test1 fail!'
        assert makeShell(2) == [[0], [0, 0], [0]], 'Test2 fail!'
        assert makeShell(3) == [[0], [0, 0], [0, 0, 0], [0, 0], [0]], (
                'Test2 fail!')

    test_makeShell()
