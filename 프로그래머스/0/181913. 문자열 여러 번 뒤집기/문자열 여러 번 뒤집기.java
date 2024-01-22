class Solution {
    public String solution(String my_string, int[][] queries) {
        for (int[] query : queries) {
            StringBuilder sb = new StringBuilder();
            int s = query[0];
            int e = query[1];
            sb.append(my_string.substring(0, s));
            for (int i = e; i >= s; i--) {
                sb.append(my_string.charAt(i));
            }
            sb.append(my_string.substring(e + 1));
            my_string = sb.toString();
        }
        return my_string;
    }
}