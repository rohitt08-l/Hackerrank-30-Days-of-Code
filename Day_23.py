import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        # Write your code here
        if root is None:
            return
        
        # Initialize the queue with the root node
        queue = [root]
        
        # Keep processing while there are nodes in the queue
        while len(queue) > 0:
            # Pop the first element from the queue
            current = queue.pop(0)
            
            # Print the current node's data followed by a space
            print(current.data, end=" ")
            
            # Enqueue left child
            if current.left is not None:
                queue.append(current.left)
                
            # Enqueue right child
            if current.right is not None:
                queue.append(current.right)
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
