import java.util.ArrayList;
import java.util.List;

class Solution {
    public int solution(int[] array) {
        int[] count = new int[1001];
        for (int i : array) {
            count[i]++;
        }

        int max = 0;
        List<Integer> maxs = new ArrayList<>();
        for (int i = 0; i < 1001; i++) {
            if (count[i] > 0) {
                if (count[i] > max) {
                    maxs = new ArrayList<>();
                    maxs.add(i);
                    max = count[i];
                } else if (count[i] == max){
                    maxs.add(i);
                }
            }
        }
        System.out.println(maxs);
        return maxs.size() > 1 ? -1 : maxs.get(0);
    }
}