import java.util.Arrays;

class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        int[] answer = {};

        switch (n) {
            case 1:
                answer = Arrays.copyOfRange(num_list, 0, slicer[1] + 1);
                break;
            case 2:
                answer = Arrays.copyOfRange(num_list, slicer[0], num_list.length);
                break;
            case 3:
                answer = Arrays.copyOfRange(num_list, slicer[0], slicer[1] + 1);
                break;
            case 4:
                answer = new int[(slicer[1] - slicer[0])/slicer[2] + 1];
                for (int i = 0; slicer[0] + slicer[2] * i <= slicer[1]; i++) {
                    answer[i] = num_list[slicer[0] + slicer[2] * i];
                }
                break;
        }
        return answer;
    }
}