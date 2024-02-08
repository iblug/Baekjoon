class Solution {
    public String solution(int age) {
        StringBuilder sb = new StringBuilder();
        while (age != 0) {
            sb.insert(0, Character.toChars(age % 10 + 'a'));
            age /= 10;
        }
        return sb.toString();
    }
}