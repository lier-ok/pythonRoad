# 字符串


if __name__ == '__main__':
    str1 = "testString"
    print(str1[0:-1])
    # str1[0] = '1'
    # print(str1)
    print("test"
          + " test1")
    print('\a')
    str1 = "hello world"
    print(str1[:6] + "lier")

    number = 100
    print(bin(number))  # 十进制转二进制
    print(oct(number))  # 十进制转八进制
    print(hex(number))  # 十进制转十六进制

    name = 'Runoob'
    print(f'Hello {name}')

    w = {"name": "lier", "url": "lier.com"}
    print(f'{w["name"]}: {w["url"]}')

    x = 2
    print(f"{x + 1}")
    print(f"{x+1=}")
