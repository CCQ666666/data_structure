from queue import Queue


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def insert_left(self, value):
        new_node = BinaryTree(value)
        if self.left_node is None:
            self.left_node = new_node
        else:
            new_node.left_node = self.left_node
            self.left_node = new_node

    def insert_right(self, value):
        new_node = BinaryTree(value)
        if self.right_node is None:
            self.right_node = new_node
        else:
            new_node.right_node = self.right_node
            self.right_node = new_node

    # 插入有序二叉树
    def insert_node(self, value):
        if value <= self.value and self.left_node:
            self.left_node.insert_node(value)
        elif value <= self.value:
            self.left_node = BinaryTree(value)
        elif value > self.value and self.right_node:
            self.right_node.insert_node(value)
        else:
            self.right_node = BinaryTree(value)

    # DFS先序遍历
    def pre_order(self):
        print(self.value)
        if self.left_node:
            self.left_node.pre_order()
        if self.right_node:
            self.right_node.pre_order()

    # DFS中序遍历
    def in_order(self):
        if self.left_node:
            self.left_node.in_order()
        print(self.value)
        if self.right_node:
            self.right_node.in_order()

    # DFS后序遍历
    def post_order(self):
        if self.left_node:
            self.left_node.post_order()
        if self.right_node:
            self.right_node.post_order()
        print(self.value)

    # BFS层遍历
    def bfs(self):
        queue = Queue()
        queue.put(self)
        while not queue.empty():
            current_node = queue.get()
            print(current_node.value)
            if current_node.left_node:
                queue.put(current_node.left_node)
            if current_node.right_node:
                queue.put(current_node.right_node)


if __name__ == '__main__':
    tree = BinaryTree('a')
    tree.left_node = BinaryTree('c')
    tree.right_node = BinaryTree('b')
    tree.insert_right('d')
    c_node = tree.left_node
    c_node.insert_left('h')
    c_node.insert_right('j')
    print('先序遍历结果如下：')
    tree.pre_order()
    print('中序遍历结果如下：')
    tree.in_order()
    print('后序遍历结果如下：')
    tree.post_order()
    print('BFS遍历结果如下：')
    tree.bfs()
    # 清空二叉树
    tree.value = None
    tree.left_node = None
    tree.right_node = None
    values = [50, 76, 21, 4, 32, 100, 64, 52]
    tree.value = values[0]
    for value in values[1:]:
        tree.insert_node(value)
    print('有序二叉树BFS遍历')
    tree.bfs()
