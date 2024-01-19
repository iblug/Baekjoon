import java.util.Stack;

class Solution {
    public int[] solution(int[] arr) {
        Stack<Integer> stk = new Stack<>();
        int i = 0;
        while (i < arr.length) {
            if (stk.isEmpty() || stk.get(stk.size()-1) < arr[i]) {
                stk.add(arr[i]);
                i++;
            } else {
                stk.pop();
            }
        }

        return stk.stream().mapToInt(n -> n).toArray();
    }
}