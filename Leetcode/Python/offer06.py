# 剑指 Offer 06. 从尾到头打印链表
# https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> list[int]:
        if head == None:
            return []
        nums = []
        while 1:
            nums.append(head.val)
            if head.next == None:
                break
            head = head.next
        nums.reverse()
        return nums


num1 = ListNode(2)
num2 = ListNode(3)
num3 = ListNode(1)

num2.next = num1
num3.next = num2

nums = ListNode([])
s = Solution()
print(s.reversePrint(None))