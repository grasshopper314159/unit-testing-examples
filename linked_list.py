class Node:
    def __init__(self, value, nextNode = None):
        self._value = value
        self._nextNode = nextNode

    def append(self, value):
        current = self
        while current.next() is not None:
            current = current.next()
        current._nextNode = Node(value)

    def contains(self, value):
        current = self
        while current is not None:
            if current.value() == value:
                return True
            current = current.next()
        return False

    # This would could easily be implemented in two different ways, one that
    # uses contains(...) and one that doesn't. The first is simpler, but the
    # second is more efficient. Unit tests help us refactor our code by
    # verifying that our changes haven't altered expected behavior.
    def delete(self, value):
        # TODO: In class
        pass

    def deleteAt(self, value, index):
        # TODO: In class
        pass

    def insert(self, value, index):
        if index == 0:
            return Node(value, self)
        # Note that this makes the test pass, but it also isn't correct. This
        # is one of the challenges of TDD, you really need to think hard about
        # your tests if you want them to be complete enough to rely upon.
        if self._nextNode is None:
            self._nextNode = Node(value)
            return self

    def next(self):
        return self._nextNode

    def value(self):
        return self._value

