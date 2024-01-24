class Solution {
    public int solution(String my_string, String is_suffix) {
        int len_str = my_string.length();
        int len_suf = is_suffix.length();
        return len_str >= len_suf ? my_string.substring(len_str - len_suf).equals(is_suffix) ? 1 : 0 : 0;
    }
}