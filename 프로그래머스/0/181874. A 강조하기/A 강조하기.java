class Solution {
    public String solution(String myString) {
        StringBuilder sb = new StringBuilder();
        for (char c : myString.toCharArray()) {
            if (c == 'a' || c == 'A') {
                sb.append('A');
            } else {
                sb.append(Character.toLowerCase(c));
            }
        }
        return sb.toString();
    }
}