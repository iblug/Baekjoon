class Solution {
    public int solution(int[] num_list) {
        StringBuilder e = new StringBuilder();
        StringBuilder o = new StringBuilder();
        for (int n : num_list) {
            if (n % 2 == 0) {
                e.append(n);
            } else {
                o.append(n);
            }
        }
        return Integer.parseInt(e.toString()) + Integer.parseInt(o.toString());
    }
}