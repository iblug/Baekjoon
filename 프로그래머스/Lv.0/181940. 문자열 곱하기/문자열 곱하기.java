import java.util.stream.IntStream;

class Solution {
    public String solution(String my_string, int k) {
        StringBuilder answer = new StringBuilder();
        IntStream.range(0, k).forEach(i -> answer.append(my_string));
        return answer.toString();
    }
}