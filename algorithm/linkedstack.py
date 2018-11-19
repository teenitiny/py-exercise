"""
File: LinkedStack.py
Author: gang
"""
from node import Node

class LinkedStack:
	def __init__(self, lyst=None):
		self._item = None
		self._size = 0
		if lyst:
			for i in lyst:
				self.push(i)
				self._size += 1

	def __iter__(self):
		cursor = self._item
		while not cursor is None:
			yield cursor.data
			cursor = cursor.next

	def __len__(self):
		return self._size

	def __str__(self):
		result = ""
		for i in self:
			result = (str(i) + " ") + result
		return result

	def clear(self):
		self._size = 0
		self._item = None

	def isEmpty(self):
		return len(self) == 0

	def push(self, item):
		self._item = Node(item, self._item)
		self._size += 1

	def pop(self):
		if self._item.next == None:
			poped = self._item.data
			self._item = None
			self._size -= 1
			return poped
		else:
			poped = self._item.data
			self._item = self._item.next
			self._size -= 1
			return poped

	def peek(self):
		return self._item.data