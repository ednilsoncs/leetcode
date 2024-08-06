# Definition for singly-linked list.

# from typing import Optional


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        old_string = ''
        new_string = ''
        len = 0
       
 
        if(current_node is None):
          return False
        
        if(current_node.next is None):
          return True
       
       
        
        while (current_node is not None):
          
          current_node = current_node.next
          len = len +1 
          old_string = old_string  + str(current_node.val)
        
        while len >= 0:
           new_string = new_string + old_string[len]
           
        
        if new_string == old_string:
           return True
        else:
           return False 
   