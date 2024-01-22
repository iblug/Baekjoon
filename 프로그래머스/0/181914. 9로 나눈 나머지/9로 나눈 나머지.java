class Solution {
    public int solution(String number) {
        int sum = 0;
        for (char c : number.toCharArray()) {
            sum += c - 48;
        }
        return sum % 9;
    }
}