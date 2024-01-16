class Solution {
    public int solution(int a, int b) {
        int x = Integer.parseInt(""+a+b);
        return Math.max(x, 2 * a * b);
    }
}