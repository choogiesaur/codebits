//https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list
/*
 * Complete the 'insertNodeAtPosition' function below.
 *
 * The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
 * The function accepts following parameters:
 *  1. INTEGER_SINGLY_LINKED_LIST llist
 *  2. INTEGER data
 *  3. INTEGER position
 */

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */

function insertNodeAtPosition(llist, data, position) {
    // Write your code here
    let newNode = new SinglyLinkedListNode(data);
    if(position == 0){
        newNode.next = llist;
        return newNode;
    }
    
    let curr = llist;
    let i = 1;
    while(i < position){
        curr = curr.next;
        i++;
    }
    let temp = curr.next;
    
    newNode.next = temp;
    curr.next = newNode;
    return llist;
}
