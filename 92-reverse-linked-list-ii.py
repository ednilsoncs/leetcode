# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        current_node = head
        node_to_add = None  
        array = []

        if(current_node is None):
            return current_node
        
        if(current_node.next is None):
            return current_node
        
        while(current_node is not None):     
          array.append(current_node.val)
          current_node = current_node.next
        
        
        array = array[:left-1] + list(reversed(array[left-1: right]))  + array[right:]
        count = len(array) - 1
        new_node = None
        while( count >= 0 ):
           new_node = ListNode(val=array[count], next= node_to_add)
           node_to_add = new_node

           count = count - 1 


        return new_node

    
