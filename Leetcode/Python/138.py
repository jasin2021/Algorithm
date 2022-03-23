# 剑指 Offer 35. 复杂链表的复制
# https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/

# 138. 复制带随机指针的链表
# https://leetcode-cn.com/problems/copy-list-with-random-pointer/



# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None 
        map = dict()
        curr = Node(0)
        curr = head
        while curr != None:
            map[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr != None:
            if curr.next == None:
                if curr.random == None:
                    map[curr].random = None
                else :
                    map[curr].random = map[curr.random]
                break
            map[curr].next = map[curr.next]
            if curr.random == None:
                map[curr].random = None
            else :
                map[curr].random = map[curr.random]
            curr = curr.next
        return map[head]

num1 = Node(2)
num2 = Node(3)
num3 = Node(1)

num2.next = num1
num3.next = num2

num3.random = None
num2.random = num1
num1.random = None


s = Solution()
print(s.copyRandomList(num3))

