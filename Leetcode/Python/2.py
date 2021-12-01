# https://leetcode-cn.com/problems/add-two-numbers/s
# 2. 两数相加

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        num2 = 0
        p = 1
        while l1:
            num1 += l1.val * p
            p *= 10
            l1 = l1.next
        p = 1
        while l2:
            num2 += l2.val * p
            p *= 10
            l2 = l2.next
        sum = str(num1 + num2)
        listSum = list(sum)
        lenth = len(listSum)
        l = ListNode(int(listSum[0]))
        for i in range(1, lenth):
            l = ListNode(int(listSum[i]), l)
            
        return l