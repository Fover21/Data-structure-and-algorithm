# 斐波那契数列是学计算机入门最经典的一道题目

# 斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）
# 以兔子繁殖为例子而引入，故又称为“兔子数列”，指的是这样一个数列：1、1、2、3、5、8、13、21、34、……在数学上，
# 斐波纳契数列以如下被以递推的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）在现代物理、准晶
# 体结构、化学等领域，斐波纳契数列都有直接的应用。

# 兔子问题（推导法可以得出规律）
# 斐波那契数列又因数学家列昂纳多·斐波那契以兔子繁殖为例子而引入，故又称为“兔子数列”。一般而言，兔子在出生两个月后，
# 就有繁殖能力，一对兔子每个月能生出一对小兔子来。如果所有兔子都不死，那么一年以后可以繁殖多少对兔子？

# 走楼梯问题（排列组合）（数学归纳法可以得到规律）
# 有一段楼梯有10级台阶，规定每一步只能跨一级或两级，要登上第10级台阶有几种不同的走法?

# 这两个问题都是典型的斐波那契数列问题


# 下面是python实现的几种方法

# 1
def func(num):
    '''
        迭代器实现fib这个效率最高，要多少直接给多少
        :param num:第几个fib的索引值
        :return: 第几个索引对应的fib值
        '''
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n = n + 1


g = func(50)
for i in range(50):
    print("第" + str(i + 1) + "个值：", g.__next__())


# 2
def fib(num):
    '''
        循环实现fib，效率比递归高
        :param num:第几个fib的索引值
        :return: 第几个索引对应的fib值
        '''
    n, a, b = 0, 0, 1
    while n < num:
        print(b)
        a, b = b, a + b
        n = n + 1


fib(50)


# 3
def fib(num):
    '''
        递归实现求fib的值，这个效率是最低的，所有的递归函数都可以用循环实现（之所以效率低是因为有一个回溯的过程）
        :param num:第几个fib的索引值
        :return: 第几个索引对应的fib值
        '''
    if num == 0:
        return 0
    else:
        return int(1 and num < 2) or fib(num - 1) + fib(num - 2)


for i in range(50):
    print(fib(i + 1))


# 4
def fib(n):
    '''
        匿名函数配合三元运算符实现求fib值
        :param num:第几个fib的索引值
        :return: 第几个索引对应的fib值
        '''
    f = lambda n, x=0, y=1: x if not n else f(n - 1, y, x + y)
    return (f(n))


for i in range(50):
    print(fib(i + 1))

