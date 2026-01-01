//https://leetcode.com/problems/rotate-list/description/
#include <iostream>
using namespace std;

/**
 * Definition for singly-linked list.
 * **/
struct ListNode {
 int val;
 ListNode *next;
 ListNode() : val(0), next(nullptr) {}
 ListNode(int x) : val(x), next(nullptr) {}
 ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
    int reduceK(ListNode* head, int k){
        if (k == 0){
            return 0;
        }
            ListNode* listName = head;
            int sizeOfList = 0;
        while(listName != nullptr){
            if(listName != nullptr){
                listName = listName -> next;
                sizeOfList += 1;
            }
        }

        if (sizeOfList != 0 && k > sizeOfList){
            int new_k;
            new_k = k % sizeOfList;
            return new_k;
        }else{
            return k;
        }

        
    }
    
    ListNode* rotateRight(ListNode* head, int k) {
        k = reduceK(head, k);
        if(head == NULL ){
            return head;
        }else if (head -> next == nullptr)
        {
            return head;
        }else if(k == 0){
            return head;
        }else{
        for(int i = 1; i <= k; i++){
            head = shiftRight(head);
        }}
        return head;
        
    }

    ListNode* shiftRight(ListNode *head){ // pointer 

        ListNode *currentNode = head;
        ListNode *currentNodePrev = currentNode;
        while(currentNode -> next != nullptr){
            currentNodePrev = currentNode;
            if (currentNode -> next == nullptr){
                break;
            }else{
                ListNode *currentNodePrev = currentNode;
                currentNode = currentNode -> next;
            }
        };

        ListNode *newHead = currentNode;
        newHead -> next = head;
        currentNodePrev -> next = nullptr;

        return newHead;
    }
};

int loopThroughList(ListNode* head){

    ListNode* listName = head;
    while(listName != nullptr){
        cout << listName -> val << endl;
        if(listName != nullptr){
            listName = listName -> next;
        }
        
        
    }
    return 0;
};



int main(void){
    ListNode* head = new ListNode(1);
    ListNode* two = new ListNode(2);
    head -> next = two;
    ListNode* three = new ListNode(3);
    two -> next = three;
    ListNode* four = new ListNode(4);
    three -> next = four;
    ListNode* five = new ListNode(5);
    four -> next = five;

    loopThroughList(head);
    cout << "\n" << endl;
    Solution test;
    head = test.rotateRight(head,2);
    loopThroughList(head);
    cout << "\n" << endl;
    int size = test.reduceK(head, 2);
    cout << size << endl;
}