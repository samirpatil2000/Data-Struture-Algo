#include<stdio.h>
#include<stdlib.h>


struct node
{
    int data;
    struct node *link;
};

struct node  *create_LinkedList(struct node *head){
    struct node *new_node ,*ptr;
    int num;
    printf("\nEnter the data in linked list ");
    printf("\n -1 for end ");
    printf("\n Enter the element : ");
    scanf("%d",&num);

    while(num != -1){
        if(head == NULL){
            new_node=malloc(sizeof(struct node));
            new_node->data=num;
            new_node->link=NULL;
            head=new_node;
        }
        else
        {
            new_node=malloc(sizeof(struct node));
            new_node->data=num;
            ptr=head;
            while(ptr->link != NULL){
                ptr=ptr->link;
            }
            ptr->link=new_node;
            new_node->link=NULL;
        }
        printf("\n Enter the element : ");
        scanf("%d",&num);
    }
    return head;
}

struct node *display(struct node *start){
    struct node *ptr;
    ptr=start;
    while(ptr!= NULL){
        printf(" %d -> ",ptr->data);
        ptr=ptr->link;
    }
    printf("\n");
    return start;
}

struct node *lastToFront(struct node *start){
    struct node *preptr=start,*ptr=preptr->link;
    
    while(ptr->link!=NULL){
        preptr=ptr;
        ptr=ptr->link;
    }
    preptr->link=NULL;
    ptr->link=start;
    start=ptr;
    return start;
}



int main(){
    struct node *head=NULL;
    head=create_LinkedList(head);
    head=display(head);
    head=lastToFront(head);
    head=display(head);
}