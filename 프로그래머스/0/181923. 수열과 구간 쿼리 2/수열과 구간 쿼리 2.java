class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int[] query = queries[i];
            int num = 1000001;
            boolean flag = false;
            for (int j = query[0]; j <= query[1]; j++) {
                if (query[2] < arr[j] && arr[j] < num) {
                    flag = true;
                    num = arr[j];
                }
            }
            answer[i] = flag ? num : -1;
        }
        return answer;
    }
}