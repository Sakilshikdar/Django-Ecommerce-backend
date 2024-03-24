#include<bits/stdc++.h>
using namespace std;

class Node{
    public:
    int val;
    Node *next;

    Node(int val){
        this->val=val;
        this->next=NULL;
    }
};

//Inserting Node to Tail Index
void insert_next(Node *&head,int val){
    Node *newNode=new Node(val);

    if(head==NULL){
        head=newNode;
        return;
    }

    Node *temp=head;
    while(temp->next!=NULL){
        temp=temp->next;
    }
    temp->next=newNode;
}


//Checking shorterd 

void mid_value(Node* head) {
    vector<int>record_element;
   
   
   Node * tmp = head;

    while (tmp != NULL) {
        record_element.push_back(tmp->val);
        tmp = tmp->next;
        }

        int len=record_element.size();
        if(len%2==1){
            cout<<record_element[(len-1)/2]<<endl;
        }else{
            cout<<record_element[(len/2)-1]<<" "<<record_element[len/2]<<endl;
        }



    // auto it = find(v.begin(),v.end(),8);
    // // cout<<*it<<endl;
    // if(it==v.end())cout<<"not Found";
    // else cout<<"Found";
}


// void print_it(Node *head){
//     Node *tmp=head;
//     while(tmp!=NULL){
//         cout<<tmp->val<<" ";
//         tmp=tmp->next;
//     }
//     cout<<endl;
// }




// int get_length(Node * head){
//     Node *tmp=head;
//     int len=0;
//     while(tmp!=NULL){
//         len++;
//         tmp=tmp->next;
//     }
//     return len;
// }



int main(){

    Node *head=NULL;

    while(true){
        int val;
        cin>>val;
        if(val==-1){
            break;
        }
        insert_next(head,val);
    }
    // if(sorted_assending(head)==true){
    //     cout<<"YES"<<endl;
    // }else{
    //     cout<<"NO"<<endl;
    // }

    mid_value(head);
    

    // int rs=get_length(head);
    // cout<<rs<<endl;

    //print_it(head);

    return 0;
}