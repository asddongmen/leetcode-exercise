'''
题目描述：
有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。
现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。

'''

# 第一种方法，从前往后走，碰到1走两步，碰到0走一步，若从倒数第二步到最后一步之间只隔了一步
# 则最后为0bit

class Solution_1(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        length = len(bits)
        i = 0
        while i < length:
            if bits[i] == 1:
                i = i + 2
                if i == length:
                    return 0
            else:
                i = i + 1 
        return 1 


# 第二种算法，从后往前走
# 若最后一个数字是1，则返回0
# 若最后一个数字是0，且倒数第二个数字为0，则返回1
# 若最后一个数字是0，且其与倒数第二个0之间1的个数为偶数个，则返回1

class Solution_2(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        length = len(bits)
        i = 2
        if bits[length - 1] == 1:
            return 0
        else:
            while bits[length - i] == 1:
                i = i + 1
            if i % 2 == 0:
                return 1
        return 0 


if __name__ == '__main__':
    bits = [1, 1, 1, 0, 0, 1, 0]
    s1 = Solution_1()
    print('第一种算法:',s1.isOneBitCharacter(bits))
    s2 = Solution_2()
    print('第二种算法:',s2.isOneBitCharacter(bits))
