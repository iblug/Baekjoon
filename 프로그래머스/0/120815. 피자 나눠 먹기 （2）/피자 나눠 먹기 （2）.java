class Solution {
    public int solution(int n) {
        int x = n;
        int y = 6;
        while (true) {
            if (x == 0) break;
            int t = x;
            x = y % x;
            y = t;
        }

        return n / y;
    }
}