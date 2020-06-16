# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def return_linked_list(l1, l2):
        l1_str = ""
        while l1 is not None:
            l1_str += str(l1.val)
            l1 = l1.next
        l1_str = int(l1_str[::-1])
        
        l2_str = ""
        while l2 is not None:
            l2_str += str(l2.val)
            l2 = l2.next
        l2_str = int(l2_str[::-1])
        
        sum_total = l1_str + l2_str
        sum_total = list(str(sum_total))
        return sum_total
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        summed = Solution.return_linked_list(l1, l2)
        start_node = None
        for i in summed:
            node = ListNode(i)
            node.next = start_node
            start_node = node
        return start_node


