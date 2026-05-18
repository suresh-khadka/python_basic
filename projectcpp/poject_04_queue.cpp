#include<iostream>
using namespace std;
#define n 10

template <class T>
class queue{
    public:
    int front,rear;
    T que[n];

    queue(): front(-1),rear(-1){}

    void enqueue(){
        int data;
        if(rear==n-1){
            cout<<"queue overflow "<<endl;

        }
        else if(front==-1 && rear==-1){
            front=0;
            rear=0;
            cout<<"enter a data to be inserted : ";
            cin>>data;
            que[rear]=data;
        }
        else{
            cout<<"enter a data to be inserted : ";
            cin>>data;
            rear+=1;
            que[rear]=data;
        }
    }

    void dequeue(){
        int data;
        if(front==-1 || front>rear){
            cout<<"Queue underflow"<<endl;

        }
        else{
            data = que[front];
            front+=1;
            cout<<"the dequeue data is : "<<data<<endl;
        }
    }

};


int main(){
    int choice;
    queue<int> q;
    cout<<"press 1 to enque..............."<<endl;
    cout<<"press 1 to deque..............."<<endl;
    while(1){
        cout<<"enter a choice : ";
        cin>>choice;
        switch(choice){
            case 0:
            q.dequeue();
            break;

            case 1:
            q.enqueue();
            break;

            default:
            cout<<"invalid enter";
            goto down;
            break;
        }


    }
    down: return 0;
}
