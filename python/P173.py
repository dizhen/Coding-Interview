# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
        
    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        node = self.stack.pop()
        temp = node
        if temp.right:
            temp = temp.right
            while temp:
                self.stack.append(temp)
                temp = temp.left
        return node.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())