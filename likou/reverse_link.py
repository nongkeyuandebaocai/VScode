pre=None
cur=head
while cur:
    temp=cur.next
    cur.next=pre
    pre=cur
    temp=cur
return pre