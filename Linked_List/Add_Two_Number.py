class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
      
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 != None or l2 != None:
            if l1 == None:
                first = 0
            else:
                first = l1.val
            if l2 == None:
                second = 0
            else:
                second = l2.val
            curr_sum = first + second + carry
            new_node = ListNode(curr_sum % 10)
            carry = curr_sum // 10
            curr.next = new_node
            curr = curr.next
            if l1 != None:
                l1 = l1.next
            if l2!= None:
                l2 = l2.next
        if carry != 0:
            new_node = ListNode(carry)
            curr.next = new_node
        return dummy.next
            
        
