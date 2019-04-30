# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        i = 0
        j = 0
        sums = 0
        
        while l1:
            sums += l1.val * (10**i)
            i += 1
            l1 = l1.next

        while l2:
            sums += l2.val * (10**j)
            j += 1
            l2 = l2.next

        head = ListNode(sums % 10)
        work = head
        sums = int(sums / 10)
        

        while sums >= 1:
            new = ListNode(sums % 10)
            sums = int(sums / 10)
            work.next = new
            work = new
        return head
