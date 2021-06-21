'''
Share
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        s1 = []
        s2 = []
        
        while l1:
            s1 += [l1.val]
            l1 = l1.next
        
        while l2:
            s2 += [l2.val]
            l2 = l2.next
        
        s = sorted(s1+s2)  #merge and sort the combined list
        
        point = head = ListNode(0)
        for k in s:
            point.next = ListNode(k)
            point = point.next
        return head.next