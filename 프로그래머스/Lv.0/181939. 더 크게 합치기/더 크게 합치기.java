class Solution {
    public int solution(int a, int b) {
        String x = String.valueOf(a);
        String y = String.valueOf(b);
        return Integer.valueOf(x + y, 10) > Integer.valueOf(y + x, 10) ? Integer.valueOf(x + y) : Integer.valueOf(y + x);
    }
}