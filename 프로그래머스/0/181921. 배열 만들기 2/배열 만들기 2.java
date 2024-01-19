import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> solution(int l, int r) {
        List<Integer> answer= new ArrayList<>();
        String[] nc = new String[]{"1", "2", "3", "4", "6", "7", "8", "9"};
        for (int i = l; i <= r; i++) {
            boolean flag = true;
            String s = String.valueOf(i);
            for (String c : nc) {
                if (s.contains(c)) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                answer.add(i);
            }
        }
        return answer.isEmpty() ? List.of(-1) : answer;
    }
}