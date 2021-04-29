class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self,data):
        if self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data
root = Node(28)
root.insert(15)
root.insert(65)
root.insert(60)
# print(root.self)