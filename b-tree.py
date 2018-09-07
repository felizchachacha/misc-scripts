#!/usr/bin/env python2

Tree={'G': 'E', 'E':'D', 'D': 'B', 'B': 'A', 'C': 'A', 'F': 'C'}


print type(Tree)

def outTree(Tree):
	print Tree

	def findFirstEnd (Tree):
		for child, parent in Tree.iteritems():
			if child not in Tree.values():
				return child
	
	while len(Tree)>0:
		end=findFirstEnd(Tree)
		child=Tree[end]
		out='('+end+')'

		while child in Tree.keys():
			parent=Tree[child]
			out='('+parent+out+')'
			del Tree[child]
			child=parent
		

		return out
			
print outTree(Tree)

