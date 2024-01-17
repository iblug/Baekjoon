import java.util.Arrays;

class Solution {
    public int solution(int[] num_list) {
        int m = Arrays.stream(num_list).reduce(1, (a, b) -> a * b);
        int s = Arrays.stream(num_list).sum();
        return m < s * s ? 1 : 0;
    }
}