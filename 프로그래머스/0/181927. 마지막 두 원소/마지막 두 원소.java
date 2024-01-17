import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        int last = num_list[num_list.length - 1];
        int pLast = num_list[num_list.length - 2];
        int len = num_list.length;
        int[] answer = Arrays.copyOf(num_list, len + 1);
        
        if (last > pLast) {
            answer[len] = last - pLast;
        } else {
            answer[len] = last * 2;
        }
        
        return answer;
    }
}