# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
                self.head = new_node

    def printll(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

if __name__ == "__main__":
    print("--------------------------------------------")
    e1 = ListNode(1)
    e2 = ListNode(2)
    ll = LinkedList(e1)
    ll.append(e2)
    print(ll)