import java.util.Arrays;

class Solution {
    public int solution(int a, int b, int c) {
        int[] arr = new int[]{a, b, c};
        Arrays.sort(arr);

        int answer = 0;
        if (arr[0] == arr[2]) {
            answer = Arrays.stream(arr).sum() * Arrays.stream(arr).map(i -> i*i).sum() * Arrays.stream(arr).map(i -> i*i*i).sum();
        } else if (arr[0] == arr[1] || arr[1] == arr[2]) {
            answer = Arrays.stream(arr).sum() * Arrays.stream(arr).map(i -> i*i).sum();
        } else {
            answer = Arrays.stream(arr).sum();
        }
        return answer;
    }
}