# 集合set
if __name__ == '__main__':
    params = {1, 2, 3, 4}
    a = [1, 2, 3, 3]
    params1 = set(a)
    print(params)
    print(params1)

    # 下面展示两个集合间的运算.
    a = set('abracadabra')
    b = set('alacazam')
    c = a - b  # 集合a中包含而集合b中不包含的元素
    d = a | b  # 集合a或b中包含的所有元素
    e = a & b  # 集合a和b中都包含了的元素
    f = a ^ b  # 不同时包含于a和b的元素

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)

    # 集合的元素操作
    set1 = {"1", "test", 3}

    # 添加
    set1.add("hulu")
    print(set1)
    # 添加，可添加列表，元组，字典等
    set1.update([1, 2], {3, 4}, (5, 6))
    print(set1)

    # 移除, 不存在会报错
    set1.remove(1)
    print(set1)
    # 移除, 不存在不会报错
    set1.discard(1)
    print(set1)

    # 随机删除
    set1.pop()
    print(set1)

    # 计算元素个数
    print(len(set1))

    # 清空集合
    set1.clear()
    print(set1)

    # 判断是否存在于集合中
    bl1 = "1" in set1
    print(bl1)