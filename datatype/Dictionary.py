# 字典
if __name__ == '__main__':
    dic = {"name":"lier","test":"testV"}
    print(dic["name"])

    dic = {"123":"test",123:456}
    print(dic[123])

    confusion = {}
    confusion[1] = 1
    confusion['1'] = 2
    confusion[1] += 1

    sum = 0
    for k in confusion:
        sum += confusion[k]

    print(sum)