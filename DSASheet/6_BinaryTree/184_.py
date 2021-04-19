
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


def preOrder(root):
    if root==None:
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
def preOrderIterative(root):
    st=[]
    curr=root
    while(len(st)>0 or curr):
        if(curr):
            print(curr.data,end=" ")
            st.append(curr)
            curr=curr.left
        else:
            curr=st.pop()
            # print(curr.data,end=" ")
            curr=curr.right
            
            
    
        
            
    
    
    


    
    
        

        

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
root.left.left=newNode(12)


root = newNode(5)
root.left = newNode(3)
root.right = newNode(6)
root.left.left = newNode(2)
root.left.left.right = newNode(1)
root.left.right = newNode(4)
display(root)

preOrder(root)
print()
preOrderIterative(root)
print()