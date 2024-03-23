class Solution {
    public String solution(String myString, String pat) {
        String answer = "";
        String subStr;
        for (int i = 0; i < myString.length(); i++) {
            subStr = myString.substring(0, i + 1);
            if (subStr.endsWith(pat)) {
                answer = subStr;
            }
        }
        return answer;
    }
}