# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinekedList:
    def __init__(self):
        self.head = None

    def insert_in_begining(self,data):
        node = ListNode(data, self.head)
        self.head = node

    def print_list(self):
        l = self.head
        while l:
            print(l.val)
            l = l.next

    def count_node(self):
        counter = 0
        l=self.head
        while l:
            counter +=1
            l=l.next

        return counter

class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        l1_len = LinekedList.count_node(l1)
        l2_len = LinekedList.count_node(l2)

        loop_range =  l1_len if l1_len>l2_len else l2_len
        node1 = l1.head
        node2 = l2.head
        carry=0
        result = LinekedList()
        for i in range(loop_range):
            val1 = node1.val if node1.val else 0
            val2 = node2.val if node2.val else 0

            sum=val2 + val1 + carry
            if sum>9:
                sum = 0
                carry = 1

            result.insert_in_begining(sum)

            node1 = node1.next if node1.next else None
            node2 = node2.next if node2.next else None


        return result


lnode1 = LinekedList()
lnode1.insert_in_begining(3)
lnode1.insert_in_begining(4)
lnode1.insert_in_begining(2)

# lnode1.print_list()


lnode2 = LinekedList()
lnode2.insert_in_begining(4)
lnode2.insert_in_begining(6)
lnode2.insert_in_begining(5)

res = Solution()
result = res.addTwoNumbers(lnode1,lnode2)
result.print_list()