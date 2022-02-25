'use strict';
// https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists
/*
    Find merge point of two linked lists
    Note that the head may be 'null' for the empty list.
    Node is defined as
    var Node = function(data) {
        this.data = data;
        this.next = null;
    }
*/

// n^2 of course, but yay for first JS problem down :^)
function findMergeNode(headA, headB) {
    let ptrA = headA;
    let ptrB = headB;
    
    while (ptrA != null) {
        ptrB = headB;
        while (ptrB != null){
            if(ptrA === ptrB){
                return ptrA.data;
            }
            ptrB = ptrB.next;
        }
        ptrA = ptrA.next;
    }
}
