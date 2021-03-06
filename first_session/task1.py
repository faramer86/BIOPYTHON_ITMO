# 1) unique()


def unique(e):
    try:
        '''
        Добавлю try/except, чтобы проверить, является ли подаваемый объект ите-
        рируемым. iff в условии сказано, что по объекту можно итерироваться.
        '''

        iter(e)
        my_list = []
        for i in e:
            if i not in my_list:
                my_list.append(i)
                my_list.sort()
        return my_list
    except TypeError as tr:
        print(tr, ': Object is not iterable')
if __name__ == '__main__':
    '''
    Пишем тесты для HW2. Каждый из тестов проверяет правильность работы функции
    unique() на разных типах данных.
    '''

    def test_list_unique():
        assert unique([1, 2, 1, 3]) == [1, 2, 3], 'Error in list'
        print('We have no trouble with lists')

    def test_str_unique():
        assert unique('abbbcbbcdb') == ['a', 'b', 'c', 'd'], 'Error in string'
        print('We have no trouble with strings')

    def test_set_unique():
        assert unique({5, 1, 3}) == [1, 3, 5], 'Error in set'
        print('We have no trouble with sets')

    test_list_unique()
    test_str_unique()
    test_set_unique()

##########################################################

# 2) transposeDict()


def transposeDict(d):
    '''
    Добавлю assert, чтобы проверить, является ли подаваемый объект словарем. В
    случае использования функции на другом типе данных, выдает ошибку.
    '''

    assert type(d) is dict, 'your variable is not dictionary!'
    d_new = dict()
    for key, value in d.items():
        d_new[value] = key
    return d_new


if __name__ == '__main__':
    '''
    Пишем тесты для HW2. Каждый из тестов проверяет правильность работы функции
    transposeDict() на разных выборках.
    '''

    def test_transposeDict():
        assert transposeDict({1: 'a', 2: 'b'}) == {'a': 1, 'b': 2}, 'ErrorDict'
        print('We have no trouble with dict number one')
        assert transposeDict({1: 1}) == {1: 1}, 'ErrorDict'
        print('We have no trouble with dict number two')
        assert transposeDict({}) == {}, 'ErrorDict'
        print('We have no trouble with dict number three')

    test_transposeDict()

##########################################################

# 3) mex()


def mex(e):
    a = 1
    while True:
        if a not in e:
            return a
        else:
            a += 1

if __name__ == '__main__':
    '''
    Пишем тесты для HW2. Каждый из тестов проверяет правильность работы функции
    mex() на разных выборках.
    '''

    def test_mex():
        assert mex([1, 2, 3]) == 4, 'Test1 - your answer is wrong!'
        print('We have no trouble with dict number one')
        assert mex(['asdf', 123]) == 1, 'Test2 - your answer is wrong!'
        print('We have no trouble with dict number two')
        assert mex([0, 0, 1, 0]) == 2, 'Test3 - your answer is wrong!'
        print('We have no trouble with dict number three')

    test_mex()

##########################################################

# 4) frequencyDict()


def frequencyDict(s):
    dict_new = dict()
    for i in s:
        dict_new[i] = s.count(i)
    return dict_new

if __name__ == '__main__':
    '''
    Пишем тесты для HW2. Каждый из тестов проверяет правильность работы функции
    frequencyDict() на разных типах данных.
    '''

    def test_frequencyDict():
        assert frequencyDict('') == {}, 'Test1Fail'
        print('We have no trouble with test number one')
        assert frequencyDict('abacab') == {'a': 3, 'b': 2, 'c': 1}, 'Test2Fail'
        print('We have no trouble with test number two')

    test_frequencyDict()
