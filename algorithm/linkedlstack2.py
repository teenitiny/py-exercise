"""
File: LinkedStack2.py
"""

from node import Node
from abstractstack import ABstractStack

class LinkedStack2(ABstractStack):
	""" link-based stack implementation."""
	def __init__(self, sourceCollection=None):
		self._items = None
		ABstractStack.__init__(self, sourceCollection)

	# Accessors
	def __iter__(self):
		"""Supports iteration over a view of self.
		Visits items from bottom to top of stack."""
		def visitNodes(node):
			if not node is None:
				visitNodes(node.next)
				temList.append(node.data)
		temList = list()
		visitNodes(self._items)
		return iter(temList)

	def peek(self):
		"""Returns the item at top of the stack.
		Precondition: the stack is not empty."""
		if self.isEmpty():
			raise KeyError("The stack is empty")
		return self._items.data

	# Mutators
	def clear(self):
		"""Makes self become empty."""
		self._size = 0
		self._items = None

	def push(self, item):
		"""Inserts item at top of the stack."""
		self._items = Node(item, self._items)
		self._size += 1

	def pop(self):
		"""Removes and returns the items at top of the stack.
		Precondition: the stack is not empty."""
		if self.isEmpty():
			raise KeyError("The stack is empty.")
		oldItem = self._items.data
		self._items = self._items.next
		self._size -= 1
		return oldItem