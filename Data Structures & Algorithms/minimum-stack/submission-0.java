class Node{
    int val;
    Node next;

    public Node(){
    }
}

class MinStack {
    Node head;
    Node curr;
    int size;
    public MinStack() {
        int size = 0;
        head = new Node();
        curr = new Node();
    }
    
    public void push(int val) {
        if(size == 0){
            head.val = val;
            head.next = null;
            curr = head;
            size++;
        }else{
            Node temp = new Node();
            temp.val = val;
            curr.next = temp;
            curr = temp;
            size++;
        }
    }
    
    public void pop() {
        if(size == 0){ return ;}
        Node ptr = head;
        if(ptr.next!=null && ptr.next.next==null){
            ptr.next = null;
            size--;
            curr = ptr;
            return;
        }
        while(ptr.next!=null && ptr.next.next!=null){
            ptr=ptr.next;
        }
        ptr.next = null;
        curr=ptr;
        size--;
    }
    
    public int top() {
        if(size==0) return 0;
        return curr.val;
    }
    
    public int getMin() {
        if(size==0) return 0;
        int min = (int) Math.pow(2,31);
        Node ptr = head;
        while(ptr!=null){
            if(ptr.val<min) min = ptr.val;
            ptr = ptr.next;
        }
        return min;
    }
}