class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        prev=None
        temp=head
        while temp:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev