# 列表
import operator
if __name__ == '__main__':
    list1 = ['Google', 'Runoob', 1997, 2000]

    print("第三个元素为 : ", list1[2])
    list1[2] = 2001
    print("更新后的第三个元素为 : ", list1[2])

    list2 = ['Google', 'Runoob', 'Taobao']
    list2.append('Baidu')
    print("更新后的列表 : ", list1)

    list3 = ['Google', 'Runoob', 1997, 2000]
    print("原始列表 : ", list3)
    del list3[2]
    print("删除第三个元素 : ", list3)

    # 列表比较

    a = [1, 2]
    b = [2, 3]
    c = [2, 3]
    d = [3, 2]
    print(operator.eq(a,b))
    print(operator.eq(c,b))
    print(operator.eq(c,d))

    a.pop(0)
    print(a)

    x = a.copy()

    print(x)
    print(type(x))