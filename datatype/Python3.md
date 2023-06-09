## Python3

### 1: 基础语法

####  **1.1: 编码**

​	python3源文件默认为utf8编码



#### **1.2: 标识符**

​	首字符必须以下划线或者字符开头,其他部分由字母数字下划线组成

​	大小写敏感



#### **1.3: python关键字**

```python
False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
```



#### 1.4: 注释

​	单行注释 # 开头	

```python
# 注释内容
```

​	多行注释 可以使用**'''** 和 **"""**

```python
''' 
注释内容1
注释内容2
'''

"""
注释内容1
注释内容2
"""
```



#### 1.5: 行与缩进

​	使用缩进来表示代码块，不需要使用大括号 **{}** 

​	同一代码块缩进空格数必须一致

```python
if True:
    print ("True")
else:
    print ("False")
```



#### 1.6: 多行语句

​	同一语句换行时,可以使用反斜杠\力所能及的

```python
total = item_one + \
        item_two + \
        item_three
```

在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \

```python
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
```



#### 1.7: 输入

```python
input(“提示信息”)
```



#### 1.8: 导入模块

​	在 python 用 **import** 或者 **from...import** 来导入相应的模块。

​	将整个模块(somemodule)导入，格式为： **import somemodule**

​	从某个模块中导入某个函数,格式为： **from somemodule import somefunction**

​	从某个模块中导入多个函数,格式为： **from somemodule import firstfunc, secondfunc, thirdfunc**

​	将某个模块中的全部函数导入，格式为： **from somemodule import \***

### 2: 数据类型



#### 2.1： 基本说明

​	Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

​	在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。

​	等号（=）用来给变量赋值。

​	等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：

```python
#!/usr/bin/python3

counter = 100      # 整型变量
miles  = 1000.0    # 浮点型变量
name   = "runoob"   # 字符串

print (counter)
print (miles)
print (name)
```

#### 2.2 ：多个变量赋值



​	Python允许你同时为多个变量赋值。例如：

```
a = b = c = 1
```

​	以上实例，创建一个整型对象，值为 1，从后向前赋值，三个变量被赋予相同的数值。

​	您也可以为多个对象指定多个变量。例如：

```
a, b, c = 1, 2, "runoob"
```

​	以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。



#### 2.3：标准数据类型

Python3 中常见的数据类型有：

- Number（数字）
- String（字符串）
- bool（布尔类型）
- List（列表）
- Tuple（元组）
- Set（集合）
- Dictionary（字典）

Python3 的六个标准数据类型中：

- **不可变数据（3 个）：**Number（数字）、String（字符串）、Tuple（元组）；
- **可变数据（3 个）：**List（列表）、Dictionary（字典）、Set（集合）。

此外还有一些高级的数据类型，如: 字节数组类型(bytes)。



#### 2.4 ：运算符

##### 	**Python算术运算符**

​		以下假设变量 **a=10**，变量 **b=21**：

| 运算符 | 描述                                            | 实例               |
| :----- | :---------------------------------------------- | :----------------- |
| +      | 加 - 两个对象相加                               | a + b 输出结果 31  |
| -      | 减 - 得到负数或是一个数减去另一个数             | a - b 输出结果 -11 |
| *      | 乘 - 两个数相乘或是返回一个被重复若干次的字符串 | a * b 输出结果 210 |
| /      | 除 - x 除以 y                                   | b / a 输出结果 2.1 |
| %      | 取模 - 返回除法的余数                           | b % a 输出结果 1   |
| **     | 幂 - 返回x的y次幂                               | a**b 为10的21次方  |
| //     | 取整除 - 往小的方向取整数                       |                    |

##### 	**Python比较运算符**

​		以下假设变量a为10，变量b为20：

| 运算符 | 描述                                                         | 实例                  |
| :----- | :----------------------------------------------------------- | :-------------------- |
| ==     | 等于 - 比较对象是否相等                                      | (a == b) 返回 False。 |
| !=     | 不等于 - 比较两个对象是否不相等                              | (a != b) 返回 True。  |
| >      | 大于 - 返回x是否大于y                                        | (a > b) 返回 False。  |
| <      | 小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。 | (a < b) 返回 True。   |
| >=     | 大于等于 - 返回x是否大于等于y。                              | (a >= b) 返回 False。 |
| <=     | 小于等于 - 返回x是否小于等于y。                              | (a <= b) 返回 True。  |

| =    | 简单的赋值运算符                                             | c = a + b 将 a + b 的运算结果赋值为 c                        |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| +=   | 加法赋值运算符                                               | c += a 等效于 c = c + a                                      |
| -=   | 减法赋值运算符                                               | c -= a 等效于 c = c - a                                      |
| *=   | 乘法赋值运算符                                               | c *= a 等效于 c = c * a                                      |
| /=   | 除法赋值运算符                                               | c /= a 等效于 c = c / a                                      |
| %=   | 取模赋值运算符                                               | c %= a 等效于 c = c % a                                      |
| **=  | 幂赋值运算符                                                 | c **= a 等效于 c = c ** a                                    |
| //=  | 取整除赋值运算符                                             | c //= a 等效于 c = c // a                                    |
| :=   | 海象运算符，可在表达式内部为变量赋值。**Python3.8 版本新增运算符**。 | 在这个示例中，赋值表达式可以避免调用 len() 两次:`if (n := len(a)) > 10:    print(f"List is too long ({n} elements, expected <= 10)")` |

| &    | 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0 | (a & b) 输出结果 12 ，二进制解释： 0000 1100                 |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| \|   | 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。 | (a \| b) 输出结果 61 ，二进制解释： 0011 1101                |
| ^    | 按位异或运算符：当两对应的二进位相异时，结果为1              | (a ^ b) 输出结果 49 ，二进制解释： 0011 0001                 |
| ~    | 按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。**~x** 类似于 **-x-1** | (~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。 |
| <<   | 左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。 | a << 2 输出结果 240 ，二进制解释： 1111 0000                 |
| >>   | 右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数 |                                                              |

| and  | x and y | 布尔"与" - 如果 x 为 False，x and y 返回 x 的值，否则返回 y 的计算值。 | (a and b) 返回 20。     |
| ---- | ------- | ------------------------------------------------------------ | ----------------------- |
| or   | x or y  | 布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。 | (a or b) 返回 10。      |
| not  | not x   | 布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。 | not(a and b) 返回 False |

| in     | 如果在指定的序列中找到值返回 True，否则返回 False。     | x 在 y 序列中 , 如果 x 在 y 序列中返回 True。     |
| ------ | ------------------------------------------------------- | ------------------------------------------------- |
| not in | 如果在指定的序列中没有找到值返回 True，否则返回 False。 | x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。 |

**Python身份运算符**

身份运算符用于比较两个对象的存储单元

| 运算符 | 描述                                        | 实例                                                         |
| :----- | :------------------------------------------ | :----------------------------------------------------------- |
| is     | is 是判断两个标识符是不是引用自一个对象     | **x is y**, 类似 **id(x) == id(y)** , 如果引用的是同一个对象则返回 True，否则返回 False |
| is not | is not 是判断两个标识符是不是引用自不同对象 | **x is not y** ， 类似 **id(x) != id(y)**。如果引用的不是同一个对象则返回结果 True，否则返回 False。 |

#### 2.5：Number（数字）

​	Python3 支持 **int、float、bool、complex（复数）**。

​	在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。

​	像大多数语言一样，数值类型的赋值和计算都是很直观的。

​	内置的 type() 函数可以用来查询变量所指的对象类型。

​	也可以用isinstance()函数判读

​	**Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加，* True==1、False==0 *会返回* 	True**

​	**在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True**

```python
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

# 输出结果
<class 'int'> <class 'bool'> <class 'float'> <class 'complex'>
true
False True

# issubclass(参数一，参数二) 函数可以用于判断参数一是否为参数二的子类
```

​	当给变量赋值时，该对象就会被创建，可以使用del删除创建的对象

```python
# del删除对象，删除后不可以在使用
    test, test1, test2 = 10, 11, 12
    del test, test1, test2
```

##### 	**数值运算**

```python
# 数值运算
    x = 5 + 4
    y = 4.3 - 2
    z = 2 * 3
    u = 2 / 3  # 结果为浮点数
    i = 2 // 3  # 结果取整数部分
    o = 2 ** 3  # 2的三次方
    print(x, y, z, u, i, o)
```

​	**注意：**

- 1、Python可以同时为多个变量赋值，如a, b = 1, 2。
- 2、一个变量可以通过赋值指向不同类型的对象。
- 3、数值的除法包含两个运算符：**/** 返回一个浮点数，**//** 返回一个整数。
- 4、***混合计算时，Python会把整型转换成为浮点数。***

Python 还支持复数，复数由实数部分和虚数部分构成，可以用 **a + bj**，或者 **complex(a,b)** 表示， 复数的实部 **a** 和虚部 **b** 都是浮点型。

| 函数            | 返回值 ( 描述 )                                              |
| :-------------- | :----------------------------------------------------------- |
| abs(x)          | 返回数字的绝对值，如abs(-10) 返回 10                         |
| ceil(x)         | 返回数字的上入整数，如math.ceil(4.1) 返回 5                  |
| cmp(x, y)       | 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 **Python 3 已废弃，使用 (x>y)-(x<y) 替换**。 |
| exp(x)          | 返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045         |
| fabs(x)         | 以浮点数形式返回数字的绝对值，如math.fabs(-10) 返回10.0      |
| floor(x)        | 返回数字的下舍整数，如math.floor(4.9)返回 4                  |
| log(x)          | 如math.log(math.e)返回1.0,math.log(100,10)返回2.0            |
| log10(x)        | 返回以10为基数的x的对数，如math.log10(100)返回 2.0           |
| max(x1, x2,...) | 返回给定参数的最大值，参数可以为序列。                       |
| min(x1, x2,...) | 返回给定参数的最小值，参数可以为序列。                       |
| modf(x)         | 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。 |
| pow(x, y)       | x**y 运算后的值。                                            |
| round(x [,n\])  | 返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。**其实准确的说是保留值将保留到离上一位更近的一端。** |
| sqrt(x)         | 返回数字x的平方根。                                          |

| 函数                               | 描述                                                         |
| :--------------------------------- | :----------------------------------------------------------- |
| choice(seq)                        | 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。 |
| randrange ([start,\] stop [,step]) | 从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1 |
| random()                           | 随机生成下一个实数，它在[0,1)范围内。                        |
| seed([x\])                         | 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。 |
| shuffle(lst)                       | 将序列的所有元素随机排序                                     |
| uniform(x, y)                      | 随机生成下一个实数，它在[x,y]范围内。                        |

| 函数        | 描述                                              |
| :---------- | :------------------------------------------------ |
| acos(x)     | 返回x的反余弦弧度值。                             |
| asin(x)     | 返回x的反正弦弧度值。                             |
| atan(x)     | 返回x的反正切弧度值。                             |
| atan2(y, x) | 返回给定的 X 及 Y 坐标值的反正切值。              |
| cos(x)      | 返回x的弧度的余弦值。                             |
| hypot(x, y) | 返回欧几里德范数 sqrt(x*x + y*y)。                |
| sin(x)      | 返回的x弧度的正弦值。                             |
| tan(x)      | 返回x弧度的正切值。                               |
| degrees(x)  | 将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0 |
| radians(x)  | 将角度转换为弧度                                  |

| 常量 | 描述                                  |
| :--- | :------------------------------------ |
| pi   | 数学常量 pi（圆周率，一般以π来表示）  |
| e    | 数学常量 e，e即自然常数（自然常数）。 |

#### 2.6：String字符串

Python中的字符串用单引号 **'** 或双引号 **"** 括起来，同时使用反斜杠 **\** 转义特殊字符。

字符串的截取的语法格式如下：

```
变量[头下标:尾下标]
```

索引值以 0 为开始值，-1 为从末尾的开始位置。

![img](https://static.runoob.com/wp-content/uploads/123456-20200923-1.svg)

加号 **+** 是字符串的连接符， 星号 ***** 表示复制当前字符串，与之结合的数字为复制的次数。实例如下：

```python
#!/usr/bin/python3

str = 'Runoob'

print (str)      # 输出字符串
print (str[0:-1])   # 输出第一个到倒数第二个的所有字符
print (str[0])    # 输出字符串第一个字符
print (str[2:5])   # 输出从第三个开始到第五个的字符
print (str[2:])    # 输出从第三个开始的后的所有字符
print (str * 2)    # 输出字符串两次，也可以写成 print (2 * str)
print (str + "TEST") # 连接字符串
```

Python 使用反斜杠 **\** 转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 **r**，表示原始字符串：

```python
print('Ru\noob')
Ru
oob
print(r'Ru\noob')
Ru\noob
```

**与 C,java 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如 xxx[0] = 'm' 会导致错误。**但可以截取其中一部分字符串使用+拼接其他字符串

```python
str1 = "hello world"
ptint(str1[:6] + "lier")
```

##### **进制转换**

```python
number = 100
    print(bin(number))  # 十进制转二进制
    print(oct(number))  # 十进制转八进制
    print(hex(number))  # 十进制转十六进制
# 输出结果
0b1100100
0o144
0x64
```

##### 常见函数

| in     | 成员运算符 - 如果字符串中包含给定的字符返回 True   | **'H' in a** 输出结果 True     |
| ------ | -------------------------------------------------- | ------------------------------ |
| not in | 成员运算符 - 如果字符串中不包含给定的字符返回 True | **'M' not in a** 输出结果 True |

*Python三引号*

python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符

```python
#!/usr/bin/python3  
para_str = """这是一个多行字符串的实例 多行字符串可以使用制表符 TAB ( \t )。也可以使用换行符 [ \n ]。 """ print (para_str)
```

以上实例执行结果为：

```
这是一个多行字符串的实例
多行字符串可以使用制表符
TAB (    )。
也可以使用换行符 [ 
 ]。
```

三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的。

一个典型的用例是，当你需要一块HTML或者SQL时，这时用字符串组合，特殊字符串转义将会非常的繁琐。

##### **f-string**

f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法。

之前我们习惯用百分号 (%):

```python
name = 'Runoob'
print('Hello %s' % name)
# 输出 'Hello Runoob'
```

**f-string** 格式化字符串以 **f** 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去

```python
name = 'Runoob'
f'Hello {name}' # 替换变量
# 输出 'Hello Runoob'

f'{1+2}'     # 使用表达式
'3'

w = {'name': 'Runoob', 'url': 'www.runoob.com'}
f'{w["name"]}: {w["url"]}'
'Runoob: www.runoob.com'
```

用了这种方式明显更简单了，不用再去判断使用 %s，还是 %d。

在 Python 3.8 的版本中可以使用 **=** 符号来拼接运算表达式与结果：

```python
x = 1
print(f'{x+1}')  # Python 3.6
# 2

x = 1
print(f'{x+1=}')  # Python 3.8
# x+1=2
```

##### Python 的字符串常用函数

| 方法及描述                                                   |
| :----------------------------------------------------------- |
| **capitalize**() 将字符串的第一个字符转换为大写              |
| **count**(str, beg= 0,end=len(string)) 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数 |
| **endswith**(suffix, beg=0, end=len(string))检查字符串是否以 suffix 结束，如果 beg 或者 end 指定则检查指定的范围内是否以 suffix 结束，如果是，返回 True,否则返回 False。 |
| **find**(str, beg=0, end=len(string)) 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1 |
| **index**(str, beg=0, end=len(string))跟find()方法一样，只不过如果str不在字符串中会报一个异常。 |
| **isalnum**() 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True，否则返回 False |
| **isalpha**()如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True, 否则返回 False |
| **isdigit**() 如果字符串只包含数字则返回 True 否则返回 False.. |
| **islower**()如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False |
| **isupper**() 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False |
| **len**(string) 返回字符串长度                               |
| **lower**()转换字符串中所有大写字符为小写.                   |
| **lstrip**()截掉字符串左边的空格或指定字符。                 |
| **max**(str) 返回字符串 str 中最大的字母。                   |
| **min**(str)返回字符串 str 中最小的字母。                    |
| **replace**(old, new , max\])把 将字符串中的 old 替换成 new,如果 max 指定，则替换不超过 max 次。 |
| **rfind**(str, beg=0,end=len(string))类似于 find()函数，不过是从右边开始查找. |
| **rindex**( str, beg=0, end=len(string))类似于 index()，不过是从右边开始. |
| **rstrip**()删除字符串末尾的空格或指定字符。                 |
| **split**(str="", num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串 |
| **startswith**(substr, beg=0,end=len(string))检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。 |
| **swapcase**()将字符串中大写转换为小写，小写转换为大写       |
| **title**() 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle()) |
| **upper**()转换字符串中的小写字母为大写                      |

#### 2.7：Bool类型

- 布尔类型只有两个值：True 和 False。
- 布尔类型可以和其他数据类型进行比较，比如数字、字符串等。在比较时，Python 会将 True 视为 1，False 视为 0。
- 布尔类型可以和逻辑运算符一起使用，包括 and、or 和 not。这些运算符可以用来组合多个布尔表达式，生成一个新的布尔值。
- 布尔类型也可以被转换成其他数据类型，比如整数、浮点数和字符串。在转换时，True 会被转换成 1，False 会被转换成 0。

```python
a = True
b = False

# 比较运算符
print(2 < 3)  # True
print(2 == 3) # False

# 逻辑运算符
print(a and b) # False
print(a or b)  # True
print(not a)   # False

# 类型转换
print(int(a))  # 1
print(float(b)) # 0.0
print(str(a))  # "True"
```

**注意:** 在 Python 中，所有非零的数字和非空的字符串、列表、元组等数据类型都被视为 True，只有 **0、空字符串、空列表、空元组**等被视为 False。因此，在进行布尔类型转换时，需要注意数据类型的真假性。



#### 2.8：列表list

```python
list = [1,2,3,4]

# 获取列表中的值
# 从左往右索引为 0 1 2 。。。
# 从右往左索引为 -1 -2 。。。
# 或者使用 list[a:b]只截取索引从a到b的列表元素
```

##### 更新列表元素

```python
#!/usr/bin/python3
 
list = ['Google', 'Runoob', 1997, 2000]
 
print ("第三个元素为 : ", list[2])
list[2] = 2001
print ("更新后的第三个元素为 : ", list[2])
 
list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print ("更新后的列表 : ", list1)
```

##### 删除列表元素

可以使用 del 语句来删除列表的的元素

```python
list3 = ['Google', 'Runoob', 1997, 2000]
    print ("原始列表 : ", list3)
    del list3[2] 
    print ("删除第三个元素 : ", list3)

# 输出结果
# 原始列表 :  ['Google', 'Runoob', 1997, 2000]
# 删除第三个元素 :  ['Google', 'Runoob', 2000]
```

##### Python列表脚本操作符

| Python 表达式                         | 结果                         | 描述                 |
| :------------------------------------ | :--------------------------- | :------------------- |
| len([1, 2, 3])                        | 3                            | 长度                 |
| [1, 2, 3] + [4, 5, 6]                 | [1, 2, 3, 4, 5, 6]           | 组合                 |
| ['Hi!'] * 4                           | ['Hi!', 'Hi!', 'Hi!', 'Hi!'] | 重复                 |
| 3 in [1, 2, 3]                        | True                         | 元素是否存在于列表中 |
| for x in [1, 2, 3]: print(x, end=" ") | 1 2 3                        | 迭代                 |

##### 嵌套列表

```python
list = [[abc,def],[ghi,jkl]]
```

##### 列表比较

列表比较需要引入 **operator** 模块的 **eq** 方法，import operator

```python
a = [1, 2]
b = [2, 3]
c = [2, 3]
d = [3, 2]
print(operator.eq(a,b)) # False
print(operator.eq(c,b)) # True
print(operator.eq(c,d)) # False
```

##### Python列表函数&方法

Python包含以下函数:

| 序号 | 函数                         |
| :--- | :--------------------------- |
| 1    | len(list) 列表元素个数       |
| 2    | max(list) 返回列表元素最大值 |
| 3    | min(list) 返回列表元素最小值 |
| 4    | list(seq)将元组转换为列表    |

Python包含以下方法:

| 序号 | 方法                                                         |
| :--- | :----------------------------------------------------------- |
| 1    | list.append(obj)在列表末尾添加新的对象                       |
| 2    | list.count(obj)统计某个元素在列表中出现的次数                |
| 3    | list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表） |
| 4    | list.index(obj) 从列表中找出某个值第一个匹配项的索引位置     |
| 5    | list.insert(index, obj)将对象插入列表                        |
| 6    | list.pop() 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值 |
| 7    | list.remove(obj) 移除列表中某个值的第一个匹配项              |
| 8    | list.reverse() 反向列表中元素                                |
| 9    | list.sort( key=None, reverse=False) 对原列表进行排序         |
| 10   | list.clear() 清空列表                                        |
| 11   | list.copy()复制列表                                          |



#### 2.9：元组tuple

​	Python 的元组与列表类似，不同之处在于**元组的元素不能修改。**

​	元组使用小括号 **( )**，列表使用方括号 **[ ]**。

​	元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

```python
tup = (1,2,3)
```

​	元组中只包含一个元素时，需要在元素后面添加逗号 **,** ，否则括号会被当作运算符使用：

```python
tup1 = (50)
type(tup1)   # 不加逗号，类型为整型
# 输出 <class 'int'>

tup1 = (50,)
type(tup1)   # 加上逗号，类型为元组
# 输出 <class 'tuple'>
```

```python
tup = (1, 2, 3)
    # tup[1] = 4 元组元素不可以修改
    # del tup[1] 元组元素不可以删除
    # del tup 元组删除后不可以使用
    print(tup)
```

**元组的运算和索引截取操作与列表一致**

##### 元组的常用函数与方法

| len(tuple) 计算元组元素个数。                |                                                              |
| -------------------------------------------- | ------------------------------------------------------------ |
| **max(tuple) 返回元组中元素最大值。**        | tuple2 = ('5', '4', '8')  max(tuple2) '8'                    |
| **min(tuple) 返回元组中元素最小值。**        | `tuple2 = ('5', '4', '8') min(tuple2) '4'  `                 |
| **tuple(iterable) 将可迭代系列转换为元组。** | `list1= ['Google', 'Taobao', 'Runoob', 'Baidu'] tuple1=tuple(list1)  tuple1 ('Google', 'Taobao', 'Runoob', 'Baidu')` |

**所谓的元组不可变与java中的string不可变类似，就算重新赋值元组，也只是内存地址发生了变化**



#### 2.10：字典Dictionary

```python
dic = {key1 : value1, key2 ： value2}

# 键必须是唯一的，但值则不必。
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字

dic = {} # 创建空字典
dic1 = dict() # 使用dict函数创建字典
```

##### 字典中值操作

```python
# 注意操作key时数据类型必须与字典一致，且数据相同但类型不同的key可以共存
# 获取字典中的值
dic = {"key1" : value1, "key2" ： value2}
print(dic['key1'])
# 若字典中没有指定的key值，则会报错

# 修改字典中的值
dic["key2"] = "values"

# 删除字典中得值
del dic["key1"]
# 清空字典
dic.clear()
# 删除字典
del dic
```

##### 字典键的特性

1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住

```python
tinydict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'} 
print ("tinydict['Name']: ", tinydict['Name'])
# 输出 tinydict['Name']:  小菜鸟
```

2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：

```python
tinydict = {['Name']: 'Runoob', 'Age': 7} 
print ("tinydict['Name']: ", tinydict['Name'])

# 以上代码使用泪飙作为键，会报错
```



#### 2.11：集合Set

集合（set）是一个***<u>无序的不重复</u>***元素序列。

可以使用大括号 **{ }** 或者 **set()** 函数创建集合

注意：***<u>创建一个空集合必须用</u>*** **set()** 而不是 **{ }**，因为 **{ }** 是用来创建一个空字典

```python
params = {1, 2, 3, 4}
a = [1,2,3,3]
params1 = set(a)
print(params) # {1,2,3,4}
print(params1) # {1,2,3}重复的元素会被删除
```

##### 集合间的运算

```python
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

# 输出结果
{'c', 'b', 'a', 'd', 'r'}
{'c', 'a', 'l', 'z', 'm'}
{'r', 'b', 'd'}
{'c', 'b', 'a', 'l', 'z', 'd', 'm', 'r'}
{'c', 'a'}
{'b', 'r', 'l', 'z', 'm', 'd'}

```

集合中元素操作

```python
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

#其他
difference()	返回多个集合的差集
intersection()	返回集合的交集
union()	返回两个集合的并集
```



#### 2.12：数据类型转换

##### 隐式类型转换

整型会想浮点数自动转换，避免精度损失

```python
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

# 输出
num_int 数据类型为: <class 'int'>
num_flo 数据类型为: <class 'float'>
num_new: 值为: 124.23
num_new 数据类型为: <class 'float'>
```

##### 隐式类型转换

```python
# int() 将数据转为int类型
x = int("3") # 3
y = int(10.50) # 10

# float() 将数据转为浮点型
x = float(1) # 1.0
y = float("3") # 3.0

# str() 将数据转为字符串
x = str(1) # "1"
y = str("2.8") "2.8"

# tuple(s) 将序列转为元组
# list(s) 将序列转为裂变
# set(s) 将序列转为集合
# dict(d) 将 (key, value)元组序列转为字典
```



### 3: 流程控制

#### 3.1条件控制

```python
if condition1:
	代码块
elif condition2:
	代码块
else:
	代码块

match...case 类似于java中的switch...case
```

#### 3.2 循环控制

```python
# while
while condition:
    代码块
    
# while...else...
while condition:
    代码块
else:
    代码块

for variable in seq
	代码块
else
    代码块
    
# range函数
# 生成指定范围内的序列
range(1,5) # 1,2,3,4
range(0,10,3) # 0,3,6,9
range(-10,-100,-30) # -10,-40,-70


# break 与 continue 与java中类似
```

### 4：推导式

#### 4.1：列表推导式

```
[表达式 for 变量 in 列表] 
[out_exp_res for out_exp in input_list]

或者 

[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]
```

- out_exp_res：列表生成元素表达式，可以是有返回值的函数。
- for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中。
- if condition：条件语句，可以过滤列表中不符合条件的值。

```python
# 获取名字长度大于5的元素，并转为大写
names = ["test", "Bob", "nilu", "diluke", "原神启动"]
res = [name.upper() for name in names if len(name) > 5]
print(res)
```

#### 4.2：字典推导式

字典推导基本格式：

```python
{ key_expr: value_expr for value in collection }
或
{ key_expr: value_expr for value in collection if condition }
```

```python
# 将列表中的元素长度大于等于4的元素 作为字典的key,元素长度作为value
names = ["test", "Bob", "nilu", "diluke", "原神启动"]
res = {key:len(key)for key in names if len(key) >= 4}
print(res)
```

#### 4.3：集合推导式

集合推导式基本格式：

```
{ expression for item in Sequence }
或
{ expression for item in Sequence if conditional }
```

```python
# 将三个数的平方作为集合中的元素
values = [10, 2, 3]
res = {value ** 2 for value in values}
print(res)
```

#### 4.4：元组推导式（生成器表达式）

元组推导式可以利用 range 区间、元组、列表、字典和集合等数据类型，快速生成一个满足指定需求的元组。

元组推导式基本格式：

```
(expression for item in Sequence )
或
(expression for item in Sequence if conditional )
```

```python
# 生成一个包含数字 1~9 的元组
res = (value for value in range(1,10))
tup = tuple(res)
print(tup)
```



```python
# 将a开头的字符串首字母大写，b开头的字符串全大写

values = ["abc", "bbc", "bbr", "acd"]
res = [value.title() if value.startswith("a") else value.upper() for value in values]
print(res)
```



5：迭代器与生成器