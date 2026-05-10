class Solution {
    public boolean isValid(String s) {
        Stack<Character> myStack = new Stack<>();
        HashMap<Character, Character> isClosed = new HashMap<>();

        isClosed.put(')', '(');
        isClosed.put(']', '[');
        isClosed.put('}', '{');

        for(char c : s.toCharArray()){
            if(isClosed.containsKey(c)){
                if(!myStack.isEmpty() && myStack.peek() == isClosed.get(c)){
                    myStack.pop();
                } else{
                    return false;
                }
            } else {
                myStack.push(c);
            }
        }
        return myStack.isEmpty();
    }
}
