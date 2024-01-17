class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int s = numer1 * denom2 + numer2 * denom1;
        int m = denom1 * denom2;

        return new int[]{s/gcd(s, m), m/gcd(s, m)};
    }

    public int gcd(int x, int y) {
        if (x > y) {
            int t = x;
            x = y;
            y = t;
        }
        if (x == 0) {
            return y;
        }
        return gcd(y % x, x);
    }

    public int lcd(int x, int y) {
        return x * y / gcd(x, y);
    }
}