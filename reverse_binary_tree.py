from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def bfs(self):
        queue = Queue()
        queue.put(self)
        while not queue.empty():
            current_node = queue.get()
            tmp_left = current_node.left
            tmp_right = current_node.right
            if tmp_left or tmp_right:
                current_node.right = tmp_left
                current_node.left = tmp_right
            if current_node.left:
                queue.put(current_node.left)
            if current_node.right:
                queue.put(current_node.right)
        return self


top = TreeNode(2)
top.left = TreeNode(3)
# top.left.left = TreeNode(4)
# top.left.right = TreeNode(5)
# top.right = TreeNode(4)
# top.right.left = TreeNode(6)
# top.right.right = TreeNode(7)
top.bfs()
