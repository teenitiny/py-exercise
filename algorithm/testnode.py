"""
File: testnode.py
Tests the Node class.
"""
from node import Node
head = None

# Add five nodes to the begining of the linked structure
for count in range(1, 6):
	head = Node(count, head)

# Print the contents of the structure
while head != None:
	print(head.data)
	head = head.next

# Traversal
probe = head
while probe != None:
	probe = probe.next

# Searching
probe = head
while probe !=None and targetItem != probe.data:
	probe = probe.next
if probe != None:
	print(targetItem)
else:
	print("targetItem not found")

# Assumes 0 <= index < n
probe = head
while index > 0:
	probe = probe.next
	index -= 1
return probe.data


# Replacement
probe = head
while probe != None and targetItem != probe.data:
	probe = probe.next
if probe != None:
	probe.data = newItem
	return True
else:
	return False

# Assumes 0 <= index < n
probe = head
while index > 0:
	probe = probe.next
	index -= 1
probe.data = newItem

# Inserting at the Begining
head = Node(newItem, head)

# Inserting at the End
newNode = Node(newItem)
if head is None:
	head = newNode
else:
	probe = head
	while probe.next != None:
		probe = probe.next
	probe.next = newNode

# Removing at the Begining
# Assumes at least one node in the structure
removedItem = head.data
head = head.next
return removedItem

# Removing at the End
# Assumes at least on node in structure
removedItem = head.data
if head.next is None:
	head = None
else:
	probe = head
	while probe.next.next != None:
		probe = probe.next
	removedItem = probe.next.data
	probe.next = None
return removedItem

# Inserting at any position
if head is None or index <= 0:
	head = Node(newItem, head)
else:
	# Search for node at position index - 1
	# or last position
	probe = head
	while index > 1 and probe.next != None:
		probe = probe.next
		index -= 1
	# Insert new node after node at position index - 1
	# or last position
	probe.next = Node(newItem, probe.next)

# Removing at any position
# Assumes that the linked structure has at least one item
if index <= 0 or head.next is None:
	removedItem = head.data
	head = head.next
	return removedItem
else:
	# Search for node at position index - 1 or
	# the next to last position
	probe = head
	while index > 1 and probe.next.next != None:
		probe = probe.next
		index -= 1
	removedItem = probe.next.data
	probe.next = probe.next.next
	return removedItem


# Circular linked structure
head = Node(None, None)
head.next = head
# Search for node at position index -1 or the last position
probe = head
while index > 0 and probe.next != head:
	probe = probe.next
	index -= -1
# Insert new node after node at position index -1 or 
# last position
probe.next = Node(newItem, probe.next)


