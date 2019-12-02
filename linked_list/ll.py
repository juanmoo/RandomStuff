# Linked List Class

# Append
# Delete Value
# Insert Top


class LLNode():
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None

    def remove(self):
        if self.l is not None:
            self.l.r = self.r

        if self.r is not None:
            self.r.l = self.l


class LL(object):
    def __init__(self):
        self.head = None

        # Later
        self.tail = None

    def insert_top(self, value):
        # Inserts new node at head
        new_node = LLNode(value)
        new_node.l = None
        new_node.r = self.head

        # No elements
        if self.tail == None:
            self.tail = new_node
        else:
            self.head.l = new_node

        self.head = new_node

    def append(self, value):
        # Inserts new node at tail
        new_node = LLNode(value)
        new_node.r = None
        new_node.l = self.tail

        # No elements
        if self.head == None:
            self.head = new_node
        else:
            self.tail.r = new_node

        self.tail = new_node

    def delete(self, value):
        current = self.head

        while (current is not None and current.value != value):
            current = current.r

        # Fixes head and tail pointers
        if current is not None and current == self.head:
            self.head = current.r

        if current is not None and current == self.tail:
            self.tail = current.l

        # Fix Pointers of left and right nodes
        current.remove()


ll = LL()
for i in range(10):
    ll.append(i)

current = ll.head
while current is not None:
    print(current.value)
    current = current.r
