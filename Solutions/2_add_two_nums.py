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

    def insert_in_last(self,data):
        node = ListNode(data)
        if self.head is None:
            self.head = node
            return

        l=self.head
        while l.next:
            l=l.next
        l.next = node

    def print_list(self):
        l = self.head
        while l:
            print(l.val)
            l = l.next

class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        temp1 = node1 = list1.head
        temp2 = node2 = list2.head
        while temp1 or temp2:
            if not temp1.next and temp2.next:
                l1.insert_in_last(0)
            elif temp1.next and not temp2.next:
                l2.insert_in_last(0)
            else:
                temp1 = temp1.next
                temp2 = temp2.next

        carry=0
        result = LinekedList()
        while node1:
            val1 = node1.val
            val2 = node2.val

            sum=val2 + val1 + carry
            if sum>9:
                sum = 0
                carry = 1

            result.insert_in_begining(sum)

            node1 = node1.next
            node2 = node2.next


        return result

#
l1 = [2,4,3]
l2 = [5,6,4]

list1 = LinekedList()
list2 = LinekedList()

for i in l1:
    list1.insert_in_last(i)
for j in l2:
    list2.insert_in_last(j)

res = Solution()
result = res.addTwoNumbers(list1,list2)
result.print_list()