import random


class DoublyLinkedListNode:
    def __init__(self, value, before=None, after=None):
        self.value = value
        self.before = before
        self.after = after


class UniqueThingsCollection:
    def __init__(self):
        self.items = []
        self.item_to_position = {}
        self.item_to_node = {}
        self.head = None
        self.tail = None

    def add(self, item):
        node = DoublyLinkedListNode(item)
        self.item_to_node[item] = node
        self.items.append(item)
        self.item_to_position[item] = len(self.items) - 1
        if self.tail:
            node.before = self.tail
            self.tail.after = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def remove(self, item):
        if item in self.item_to_node:
            node = self.item_to_node[item]
            if node.after and node.before:
                node.before.after = node.after.before
                node.after.before = node.before.after
            elif node.after and not node.before:
                self.head = node.after.before
                node.after.before = None
            elif not node.after and node.before:
                self.tail = node.before
                node.before.after = None
            else:
                self.head = None
                self.tail = None

            del self.item_to_node[item]

            position = self.item_to_position.pop(item)
            last_item = self.items.pop()
            if position != len(self.items):
                self.items[position] = last_item
                self.item_to_position[last_item] = position

    def get_last(self):
        if self.tail:
            return self.tail.value
        else:
            return None

    def get_random(self):
        if len(self.items):
            return random.choice(self.items)
        else:
            return None

    def __contains__(self, item):
        if item in self.item_to_node:
            return True
        else:
            return False
