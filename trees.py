class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def preorder(root):
    if root!=None:
        preorder(root.left)
        print(root.value)
        preorder(root.right)
def levelorder(root):
    res=[]
    if root==None:
        return
    queue=[]
    queue.append(root)
    while(len(queue)!=0):
        curr=queue.pop(0)
        print(curr.value)
        if curr.left!=None:
            queue.append(curr.left)
        if curr.right!=None:
            queue.append(curr.right)
        res.append(curr.value)
    print(res)
root=node('a')
root.left=node('b')
root.right=node('c')
root.left.left=node('d')
root.left.right=node('e')
root.right.left=node('f')
root.right.right=node('g')
print("Tree Traversal:")
levelorder(root)
preorder(root)  
