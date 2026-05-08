'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self, head1, head2):
        dummy=Node(0)
        current=dummy
        
        while head1 and head2:
            if head1.data<=head2.data:
                current.next=head1
                head1=head1.next
            
            else:
                current.next=head2
                head2=head2.next
            current=current.next
            if head1:
                current.next=head1
            else:
                current.next=head2
            
      
        return dummy.next 
        