class SingleLinkedListNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"

class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""

        node = SingleLinkedListNode(obj, None)
        if self.begin is None:
            self.begin = node
        elif self.end is None:
            self.end = node
            self.begin.next = node
        else:
            self.end.next = node

    def pop(self):
        """Removes the last item and returns it."""
        pass

    def shift(self, obj):
        """Another name for push."""
        pass

    def unshift(self):
        """Removes the first item and returns it."""
        pass

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        pass

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        pass

    def last(self):
        """Returns a reference to the last item, does not remove."""
        pass

    def count(self):
        """Counts the number of elements in the list."""
        if self.begin is None:
            return 0
        if self.begin and self.end is None:
            return 1


        next_node = self.begin.next
        count = 0
        while next_node:
            count += 1
            next_node = next_node.next
        print ('counted_colors', count)
        return count


    def get(self, index):
        """Get the value at index."""
        pass

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        pass
