class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        '''
        You are given the heads of two sorted linked lists list1 and list2.
        Merge the two lists into one sorted list. The list should be made by splicing
        together the nodes of the first two lists.
        Return the head of the merged linked list.
        >>> mergeTwoLists([1,2,4], [1,3,4])
        >>> [1,1,2,3,4,4]
        '''
        