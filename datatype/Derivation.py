# 推导式
import operator
if __name__ == '__main__':
    # names = ["test", "Bob", "nilu", "diluke", "原神启动"]
    # res = [name.upper() for name in names if len(name) > 4]
    # print(res)
    #
    # cons = [data for data in range(0,30) if data % 3 == 0]
    # print(cons)

    # names = ["test", "Bob", "nilu", "diluke", "原神启动"]
    # res = {key:len(key)for key in names if len(key) >= 4}
    # print(res)

    # values = [10, 2, 3]
    # res = {data:data ** 2 for data in values}
    # print(res)

    # values = [10, 2, 3]
    # res = {value ** 2 for value in values}
    # print(res)

    # list = ["abc", "abcd", "abca", "abc"]
    # res = {value for value in list if not(operator.eq(value,"abc"))}
    # print(res)

    # res = (value for value in range(1,10))
    # tup = tuple(res)
    # print(tup)

    values = ["abc", "bbc", "bbr", "acd"]
    res = [value.title() if value.startswith("a") else value.upper() for value in values]
    print(res)