class linked_list():

    def __init__(self, head = None):
        self.head = head

    # Inner class that defines list node
    class list_node():
        def __init__(self, data):
            self.data = data
            self.next = None

        # Overloading < operator
        def __lt__(self, other):
            return True if self.data < other.data else False

        # Overloading > operator
        def __gt__(self, other):
            return True if self.data < other.data else False

        def __rshift__(self, other):
            pass

        def __lshift__(self, other):
            pass

    # Creates node from data and appends it
    def append(self, data):

        new_node = self.list_node(data)
        if self.head == None:
            self.head = new_node
            return

        head = self.head
        while head.next:
            head = head.next

        head.next = new_node

    # Strictly appends a node
    def append_node(self, node):
        head = self.head
        while head.next:
            head = head.next
        
        head.next = node

    def __str__(self):
        head = self.head
        str_rep = ''
        while head:
            str_rep += ' ' + str(head.data)
            head = head.next
        return str_rep

lst = linked_list()
lst.append(4)
lst.append(5)
print(lst)
lst.append(7)
lst.append(11)
print(lst)

print(lst.head < lst.head.next)
print(lst.head > lst.head.next)
