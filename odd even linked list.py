'''
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:

n == number of nodes in the linked list
0 <= n <= 104
-106 <= Node.val <= 106


'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a,b,c=head,[],[]
        while a:
            b.append(a.val)
            a=a.next
        a=head
        for i in range(0,len(b),2):
            c.append(b[i])
        for i in range(1,len(b),2):
            c.append(b[i])
        for i in c:
            a.val=i
            a=a.next
        return head    