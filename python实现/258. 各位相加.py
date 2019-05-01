'''
题目描述：
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
'''

# 第一种算法
# 
# 把整数转化成字符串，然后把字符串拆分成整数列表，求和
class Solution_1(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(str(num)) > 1:
            num = sum([int(i) for i in str(num) ])
        return num 

'''
第二种方法：
假如一个三位数'abc'，其值大小为s1 = 100 * a + 10 * b + 1 * c。
将此数每一位相加，变为s2 = a + b + c。
差值 diff = (s1 -s2) = 99 * a + 9 * b。
差值可以被9整除，若采用循环方式，则每次循环都把上一个数缩小了9的倍数。
所以若num<9，直接返回num;
若num > 9
如果能被9整除，则返回9（因为若s1能被9整除，s2 = s1 - (s1 - s2) 也可以被9整除 ， 所以sn可以被9整除）
如果不能被9整除，就返回被9除的余数。
'''
class Solution_2(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 9:
            return num
        else:
            v = num % 9
            if v == 0:
                return 9
            else:
                return v 


if __name__ == '__main__':
    pass
    s1 = Solution_2()
    print(s1.addDigits(11))


