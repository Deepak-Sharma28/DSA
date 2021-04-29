class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def insertleft(self,data):
        if self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            self.data = data

    def insertright(self,data):
        if self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insertright(data)
        else:
            self.data = data

root = Node(28)
root.insertleft(15)
root.insertright(65)
root.insertright(60)
# print(root.self)