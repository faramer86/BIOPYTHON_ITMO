1) unique()

def unique(my_list):
    my_list = list(my_list)
    z = len(my_list) - 1
    for i in range(0,z):
            for j in range(0,z-i):
                if my_list[j] > my_list[j+1]:
                    my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    my_list = list(set(my_list))
    my_list.sort()
    return my_list

print(unique([1, 2, 1, 3])) # [1, 2, 3]
print(unique({5, 1, 3})) # [1, 3, 5]
print(unique('adsfasdf')) # ['a', 'd', 'f', 's']

##########################################################

2) transposeDict()

def transposeDict(d):
    d_new = dict()
    for key, value in d.items():
        d_new[value] = key
    return d_new
    
print(transposeDict({1: 'a', 2: 'b'})) # {'a': 1, 'b': 2}
print(transposeDict({1: 1})) # {1: 1}
print(transposeDict({})) # {}

##########################################################

3) mex()

def mex(e):
    a = 1
    while True:
        if a not in e:
            return a
        else:
            a+=1
        
print(mex([1, 2, 3])) # 4
print(mex(['asdf', 123])) # 1
print(mex([0, 0, 1, 0])) # 2

##########################################################

4) frequencyDict()

def frequencyDict(s):
    dict_new = dict()
    for i in s:
        dict_new[i] = s.count(i)
        
    return dict_new
    
print(frequencyDict('')) # {}
print(frequencyDict('abacaba')) # {'a': 4, 'b': 2, 'c': 1}
