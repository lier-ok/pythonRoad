# python3 数据类型
if __name__ == '__main__':
    a, b, c, d = 111, True, 1.3, 2 + 3j
    print(type(a), type(b), type(c), type(d))
    e = isinstance(a, int)
    if e:
        print('true')

    # isinstance与type函数区别
    f = type(b) == int
    g = isinstance(b, int)
    print(f, g)
    # b为bool类型，bool为int子类，但是type函数不认为子类是父类的一种类型
    # 而isinstance认为子类是父类的一种类型

    # del删除对象,删除后不可使用
    test, test1, test2 = 10, 11, 12
    del test, test1, test2

    # 数值运算
    x = 5 + 4
    y = 4.3 - 2
    z = 2 * 3
    u = 2 / 3  # 结果为浮点数
    i = 2 // 3  # 结果取整数部分
    o = 2 ** 3  # 2的三次方
    print(x, y, z, u, i, o)
