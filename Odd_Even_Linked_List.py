#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




class Solution:
        def oddEvenList(self, head: ListNode) -> ListNode:
                if head is None:
                        return head
                odd = head
                even_start = even = head.next
                while odd and odd.next and even and even.next:
                        odd.next = odd.next.next
                        even.next = even.next.next
                        odd = odd.next
                        even = even.next
                odd.next = even_start
                return head
                        