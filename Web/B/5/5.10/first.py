class Node(object):
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return f"[Node with value {self.value}]"


def print_linked_list(head):
    cur = head
    while cur is not None:
        cur = cur.next
    return head


def reversed_linked_list(head):
    cur = head
    prev = None
    while cur is not None:
        nxt = cur.next
        cur.next = prev

        prev = cur
        cur = nxt
    head = prev
    return head


h, a, b, c, d = Node(1), Node(2), Node(3), Node("Внезапно"), Node(5)
h.next = a
a.next = b
b.next = c
c.next = d
print(print_linked_list(h))
h = reversed_linked_list(h)
print("---")
print(print_linked_list(h))
