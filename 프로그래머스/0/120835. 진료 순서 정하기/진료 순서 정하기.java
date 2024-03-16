import java.util.Arrays;

class Solution {
    public int[] solution(int[] emergency) {
        int len = emergency.length;
        int[] emergency_sort = Arrays.copyOf(emergency, len);
        Arrays.sort(emergency_sort);

        int[] answer = new int[len];
        for (int i = 0; i < emergency.length; i++) {
            for (int j = 0; j < emergency.length; j++) {
                if (emergency_sort[i] == emergency[j]) {
                    answer[j] = len - i;
                }
            }
        }
        return answer;
    }
}