import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr) {
        int start = -1, end = -1;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 2) {
                if (start < 0) {
                    start = i;
                }
                end = i;
            }
        }
        if (end < 0) {
            return new int[]{-1};
        } else {
            return Arrays.copyOfRange(arr, start, end + 1);
        }
    }
}