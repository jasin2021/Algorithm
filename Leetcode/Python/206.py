# 剑指 Offer 24. 反转链表
# https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/

# https://leetcode-cn.com/problems/reverse-linked-list/
# 206. 反转链表

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        prev = None
        curr = head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

num1 = ListNode(2)
num2 = ListNode(3)
num3 = ListNode(1)

num2.next = num1
num3.next = num2


s = Solution()
print(s.reverseList(num3))


            