import java.io.IOException;
import java.util.Arrays;

public class Main {
    static int[][] data;
    static int[] dp;
    static int n;

    public static void main(String[] args) throws IOException {
        n = readInt();

        data = new int[n][];
        for (int i = 0; i < n; i++) {
            data[i] = new int[2];
            data[i][0] = readInt();
            data[i][1] = readInt();
        }
        Arrays.sort(data, (o1, o2) -> o1[0] - o2[0]);

        System.out.println(solution());
    }

    private static int solution() {
        dp = new int[n];
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (data[i][1] > data[j][1]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }
        return n - Arrays.stream(dp).max().getAsInt();
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        if (v == 13) {
            System.in.read();
        }
        return t;
    }
}