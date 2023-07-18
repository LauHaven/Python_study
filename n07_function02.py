# 浅拷贝和深拷贝
# 浅拷贝：不拷贝子对象的内容，只拷贝子对象的引用copy
# 深拷贝：会连子对象的内存也全部拷贝一份，对子对象的修改不会影响源对象deepcopy

import copy as cp


# 第一种操作
# 变量a和b指向了同一个id，是同一个对象
def fun01():
    print("--------- b=a----------")
    a = [10, 20, [1, 2]]
    b = a
    b.append(30)
    b[2].append(3)
    print("a=", a, "id(a)=", id(a))  # a= [10, 20, [1, 2, 3], 30] id(a)= 2047820649792
    print("b=", b, "id(b)=", id(b))  # b= [10, 20, [1, 2, 3], 30] id(b)= 2047820649792


fun01()


# 第二种浅拷贝，a只拷贝了b对象的内容，但不拷贝a的子对象的内用，仍然保留了a的引用。
def fun02():
    print("--------- b=cp.copy(a)----------")
    a = [10, 20, [3, 4]]
    b = cp.copy(a)
    b.append(30)
    b[2].append(5)
    print("a=", a, "id(a)=", id(a))  # a= [10, 20, [3, 4, 5]] id(a)= 2047820657152
    print("b=", b, "id(b)=", id(b))  # b= [10, 20, [3, 4, 5], 30] id(b)= 2047820657408


fun02()


# 第三种深拷贝，a和b是两个完全不同的对象
def fun03():
    print("--------- b=cp.deepcopy(a)----------")
    a = [10, 20, [3, 4]]
    b = cp.deepcopy(a)
    b.append(30)
    b[2].append(5)
    print("a=", a, "id(a)=", id(a))  # a= [10, 20, [3, 4]] id(a)= 2047820649792
    print("b=", b, "id(b)=", id(b))  # b= [10, 20, [3, 4, 5], 30] id(b)= 2047820657152


fun03()

# 传递不可变对象时，如果发生拷贝是浅拷贝
#