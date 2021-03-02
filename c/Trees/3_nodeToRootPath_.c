#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct node {
    int data;
    struct node *left;
    struct node *right;
};
 
/* Function to create a new node */
 
struct node *CreateNode(int data)
{
    struct node *newNode=malloc(sizeof(struct node));
    if (!newNode) {
        return NULL;
    }
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}
void inorder(struct node *temp)
{
    if (temp == NULL)
        return;
 
    inorder(temp->left);
    printf("%d\t",temp->data);
    inorder(temp->right);
}


void display(struct node *root){
    int node_left=0,node_right=0;
    if(root==NULL){
        return;
    }
    if(root->left !=NULL){
        node_left=root->left->data;
    }
    if(root->right !=NULL){
        node_right=root->right->data;
    }
    printf(" <- %d <-- %d --> %d --> \n",node_left,root->data,node_right);
    display(root->left);
    display(root->right);
}


void nodeToRoot(struct node *root,int target,char str_[]){
    if(root==NULL){
        return;
    }
    if(root->data==str_[]){
        printf(str_);
        return;
    }
    int num = root->data;
    char snum[5];

    // convert 123 to string [buf]
    
    if(root->left !=NULL){
        nodeToRoot(root->left,target,strcat(str_,itoa(num, snum, 10)));
    }
    if(root->right !=NULL){
        nodeToRoot(root->right,target,strcat(str_,itoa(num, snum, 10)));
    }
}

int main(){
    struct node *root = CreateNode(50);
    root->left = CreateNode(25);
    root->left->left = CreateNode(12);
    root->left->right = CreateNode(37);
    root->left->right->left = CreateNode(30);
    root->right = CreateNode(75);
    root->right->left = CreateNode(62);
    root->right->left->right = CreateNode(70);
    root->right->right = CreateNode(57);

    inorder(root);
    printf("\n");
    display(root);
    nodeToRoot(root,70,"");

}
