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
        l=self.head
        while l.next:
            l=l.next
        node = ListNode(data)
        self.next = node

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

        temp1 = node1 = l1.head
        temp2 = node2 = l2.head
        while temp1 or temp2:
            if not temp1.next and temp2.next:
                l1.insert_in_last(0)
            elif temp1.next and not temp2.next:
                l2.insert_in_last(0)
            else:
                temp1 = temp1.next
                temp2 = temp2.next

        # l1_len = LinekedList.count_node(l1)
        # l2_len = LinekedList.count_node(l2)
        #
        # loop_range = l1_len if l1_len>l2_len else l2_len
        # least_node_list = l1_len if l1_len<l2_len else l2_len
        #
        # # for i in range(least_node_list,loop_range):
        # #     LinekedList.insert_in_last(0)


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


lnode1 = LinekedList()
lnode1.insert_in_begining(3)
lnode1.insert_in_begining(4)
# lnode1.insert_in_begining(2)
lnode1.print_list()


lnode2 = LinekedList()
lnode2.insert_in_begining(4)
lnode2.insert_in_begining(6)
lnode2.insert_in_begining(5)

res = Solution()
result = res.addTwoNumbers(lnode1,lnode2)
result.print_list()