class Solution {
    public int[] solution(int[] num_list, int n) {
        int[] answer = new int[(num_list.length + n - 1)/n];
        for (int i = 0, j = 0; j < num_list.length; j += n) {
            answer[i++] = num_list[j];
        }
        return answer;
    }
}