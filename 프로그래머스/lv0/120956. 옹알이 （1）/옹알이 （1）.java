class Solution {
    public int solution(String[] babbling) {
        String[] word = new String[] {"aya", "ye", "woo", "ma"};
        int cnt = 0;
        for (String b : babbling) {
            for (String w : word) {
                if (b.contains(w)) {
                    b = b.replace(w, "*");
                }
            }
            b = b.replace("*", "");
            if (b.equals("")) {
                cnt++;
            }
        }
        return cnt;
    }
}