'''
题目描述：
给定两个二进制字符串，返回他们的和（用二进制表示）。
输入为非空字符串且只包含数字 1 和 0。
'''

# 第一种方法 直接用python的内置函数
# 字符串转数字
# bin() 返回一个整数 int 或者长整数 long int 的二进制表示。 
# bin(10) --> '0b1010'
# class int(x, base=10) 

class Solution_1(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2) + int(b,2))[2:]


# 第二种方法 以后再写

class Solution_2(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """


if __name__ == '__main__':
    s = Solution_1()
    a = '111'
    b = '1'
    print(s.addBinary(a, b))