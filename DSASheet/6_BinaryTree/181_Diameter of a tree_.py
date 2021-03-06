
class newNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def display(head):
    left_node=0.0
    right_node=0.0
    if not head:
        return
    if(head.left):
        left_node=head.left.data
    if(head.right):
        right_node=head.right.data
    print(left_node,"<-",head.data,"->",right_node)
    display(head.right)
    display(head.left)


def height(root):
    if root==None:
        return -1
    return max(height(root.left),height(root.right))+1
    
        
def diameter(root):
    if root==None:
        return -1,0
    l_height,l_diameter=diameter(root.left)  
    r_height,r_diameter=diameter(root.right)
    self_height=max(l_height,r_height)+1
    self_diameter=max(l_height+r_height+2,l_diameter,r_diameter)
    # print(l_height,r_height,root.data)
    return self_height,self_diameter


    
    
        

        

root = newNode(50)
root.left=newNode(25)
root.right=newNode(75)
root.right.right=newNode(87)
root.right.left=newNode(62)
root.right.left.right=newNode(70)
root.right.left.left=newNode(60)
root.left.right=newNode(37)
root.left.right.left=newNode(30)
root.left.right.right=newNode(40)
# root.left.right.right.right=newNode(40)
root.left.left=newNode(12)
# display(root)
# print(height(root))


print(diameter(root))
