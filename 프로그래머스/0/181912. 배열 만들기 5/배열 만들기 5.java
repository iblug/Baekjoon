import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        List<Integer> answer = new ArrayList<>();
        for (String str : intStrs) {
            int x = Integer.parseInt(str.substring(s, s + l));
            if (x > k) {
                answer.add(x);
            }
        }
        return answer.stream().mapToInt(n -> n).toArray();
    }
}