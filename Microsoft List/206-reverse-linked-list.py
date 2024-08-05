# Definition for singly-linked list.

# from typing import Optional


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        node_to_add = None
 
        if(current_node is None):
          return current_node
        
        if(current_node.next is None):
          return current_node
       
       
        
        while (current_node is not None):

          #1, none
          new_node = ListNode(val=current_node.val, next= node_to_add)
          
          #2, 1 
          node_to_add = new_node
          
          current_node = current_node.next
        
        
        return new_node    
   