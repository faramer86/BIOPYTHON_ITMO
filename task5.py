#  1)def permutations(n)


def permutations(n):
    def list_gen(n, new_list=[]):
        if len(new_list) == n:
            yield tuple(new_list)
        else:
            for i in range(1, n+1):
                if i not in new_list:
                    yield from list_gen(n, new_list + [i])
    return list(list_gen(n))

#  2)def correctbracketsequences(n)


def correctbracketsequences(n):
    def list_gen(left, right=None):
        if right is None:
            right = left
        if left == right == 0:
            yield ""
        else:
            if left > 0:
                for p in list_gen(left-1, right):
                    yield "(" + p
            if right > left:
                for p in list_gen(left, right-1):
                    yield ")" + p
    return list(list_gen(n))

#  3)combinationswithrepeats(n, k)


def combinationswithrepeats(n, k):
    def list_gen(n, k, new_list=[]):
        if len(new_list) == k:
            yield tuple(new_list)
        else:
            m = max(new_list) if len(new_list) > 0 else 1
            for i in range(m, n + 1):
                yield from list_gen(n, k, new_list + [i])
    return list(list_gen(n, k))

#  4)unorderedpartitions(n)


def unorderedpartitions(n):
    def list_gen(n, pref=[]):
        if sum(pref) == n:
            yield tuple(pref)
        else:
            if pref:
                x = pref[-1]
            else:
                x = 1
            for i in range(x, n - x + 2):
                if sum(pref + [i]) <= n:
                    yield from list_gen(n, pref + [i])
    return list(list_gen(n))
