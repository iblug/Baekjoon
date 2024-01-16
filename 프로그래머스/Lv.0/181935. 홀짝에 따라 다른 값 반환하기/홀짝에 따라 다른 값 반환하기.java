import java.util.stream.IntStream;

class Solution {
    public int solution(int n) {
        int answer = 0;

        for (int i = n; i > 0; i-= 2) {
            answer += i * (n % 2 == 0 ? i : 1);
        }
        
        return answer;
    }
}