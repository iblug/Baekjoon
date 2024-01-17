class Solution {
    public String solution(int[] numLog) {
        StringBuilder answer = new StringBuilder();
        int start = numLog[0];
        for (int n : numLog) {
            int g = n - start;
            answer.append(g == 1 ? 'w' : g == -1 ? 's' : g == 10 ? 'd' : g == -10 ? 'a' : "");
            start = n;
        }
        return answer.toString();
    }
}